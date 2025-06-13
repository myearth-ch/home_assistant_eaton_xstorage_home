import aiohttp
import logging
from homeassistant.helpers.storage import Store

_LOGGER = logging.getLogger(__name__)

class EatonBatteryAPI:
    def __init__(self, hass, host, api_key, app_id, name, manufacturer, access_level="basic"):
        self.hass = hass
        self.host = host
        self.api_key = api_key
        self.app_id = app_id
        self.name = name
        self.manufacturer = manufacturer
        self.access_level = access_level
        self.access_token = None
        self.store = Store(hass, 1, f"{host}_token")

    async def connect(self):
        url = f"https://{self.host}/api/external/connect"
        headers = {
            "Authorization": f"ApiKey {self.api_key}"
        }
        body = {
            "appId": self.app_id,
            "name": self.name,
            "accessLevel": self.access_level,
            "manufacturer": self.manufacturer
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=body, headers=headers, ssl=False) as response:
                result = await response.json()
                if result.get("successful") and "accessToken" in result.get("result", {}):
                    self.access_token = result["result"]["accessToken"]
                    await self.store_token()
                    _LOGGER.info("Connected successfully. Access token acquired.")
                else:
                    _LOGGER.warning("Connection request sent, but access not yet granted.")

    async def store_token(self):
        await self.store.async_save({"access_token": self.access_token})

    async def load_token(self):
        data = await self.store.async_load()
        if data:
            self.access_token = data.get("access_token")

    async def refresh_token(self):
        _LOGGER.info("Refreshing access token...")
        await self.connect()

    async def make_request(self, method, endpoint, **kwargs):
        url = f"https://{self.host}{endpoint}"
        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {self.access_token}"
        kwargs["headers"] = headers
        kwargs["ssl"] = False  # <--- This is critical

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, **kwargs) as response:
                if response.status == 401:
                    _LOGGER.warning("Access token expired. Refreshing token...")
                    await self.refresh_token()
                    headers["Authorization"] = f"Bearer {self.access_token}"
                    kwargs["headers"] = headers
                    async with session.request(method, url, **kwargs) as retry_response:
                        return await retry_response.json()
                return await response.json()


    async def get_status(self):
        return await self.make_request("GET", "/api/external/status")

    async def get_data(self):
        return await self.make_request("GET", "/api/external/metrics??params=temp,etoday,vbat,ibat,mtf,vpv1,ipv1,iac,fac,pac,pload,etotal,htotal,edraw,grid_code,vbus,vpv2,ipv2")

