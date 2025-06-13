import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .api import EatonBatteryAPI
from .coordinator import EatonXstorageHomeCoordinator
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    return True  # Not used for config flow-based setup

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    _LOGGER.debug("Setting up Eaton xStorage Home from config entry.")
    api = EatonBatteryAPI(
        hass=hass,
        host=entry.data["host"],
        api_key="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJ0aGlyZFBhcnR5TmFtZSIsImlzcyI6ImVhdG9uZGV2QHViaXdoZXJlLmNvbSIsImV4cCI6MTg2ODQ2ODYzNSwiaWF0IjowLCJwcm9maWxlIjoidGVzdGVyIn0.qlzMHZJNqi0Tbjo5TmV6KOckDoTefLH6n1wOzyTYoqE25ng3k1cPa8JYsfLcw1As-yY8D-xh9VRehjTK7Q4Z5rYF-55gOzhQdgI_mOkys8BBfp36Ghx_z42jbXKBbZyoo3ua7O-8IY8yIZyzptxyhd6XZGiB7lRNViK4RiKVemPK-R3cspXl293KQe0F0qfKgyWAXu0ErGn0QtzSimCgsGLl16D9jmjtIqNa4n6-u4cnSMCFjKPLvZP5-NfkuPObjFGk-qsaLrQujLIIuizKRbxeFGn74bkUUJzTv2cK4jc1FnTqi_P7wSXTG2dl7Sn2__8HRu3DGQEmG0SVEV1_fya5IHzL6jrLJOpKY7W-WuSJsr1N9gCj2zu-y9YYOTDCMRJRkfDxFinSlbuvVhhTbpW9acPk7SkTP00gepINM4cLbAo7JvqgPs21KJmlNV_aAkMqvw8vkkAzqM1B7BuFgQe7zeMCxF1s139_4wx8b2vRjxzSYhbmD1WMeCWO8zaxufaVqUTyxFtN7iWiZ_Fx1y0eQgeE_0DpY0EqFbsRXy7p1mXow_iIIfG2WjLrxJ2LG2lnFR1-DGpWSFyu5A9saKj75Tumc7EgAu1mFoBFZpoh0MiNSbVrFMjTpU0iyucA038QlgALrGTJ4eZb-CM-DriMjwhu3Vli4XZAHfCxO-U",
        app_id="com.eaton.xstorageHome",
        name="Eaton xStorage Home",
        manufacturer="Eaton"
    )
    await api.connect()
    coordinator = EatonXstorageHomeCoordinator(hass, api)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["coordinator"] = coordinator

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    return True
