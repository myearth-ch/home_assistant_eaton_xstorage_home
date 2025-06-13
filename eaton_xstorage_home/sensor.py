import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import (
    PERCENTAGE,
    UnitOfPower,
)

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SENSOR_TYPES = {
    "batteryStateOfCharge": {
        "name": "Battery State of Charge",
        "unit": PERCENTAGE,
        "device_class": "battery",
    },
    "batteryPower": {
        "name": "Battery Power",
        "unit": UnitOfPower.WATT,
        "device_class": "power",
    },
    "gridPower": {
        "name": "Grid Power",
        "unit": UnitOfPower.WATT,
        "device_class": "power",
    },
    "operationMode": {
        "name": "Operation Mode",
        "unit": None,
        "device_class": None,
    },
}

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN]["coordinator"]
    entities = []

    for key, description in SENSOR_TYPES.items():
        entities.append(EatonXStorageSensor(coordinator, key, description))

    async_add_entities(entities)

class EatonXStorageSensor(SensorEntity):
    def __init__(self, coordinator, key, description):
        self.coordinator = coordinator
        self._key = key
        self._name = description["name"]
        self._unit = description["unit"]
        self._device_class = description["device_class"]

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return f"eaton_xstorage_{self._key}"

    @property
    def state(self):
        try:
            return self.coordinator.data.get(self._key)
        except Exception as e:
            _LOGGER.error(f"Error retrieving state for {self._key}: {e}")
            return None

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def device_class(self):
        return self._device_class

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.coordinator.api.host)},
            "name": "Eaton xStorage Home",
            "manufacturer": "Eaton",
            "model": "xStorage Home",
            "entry_type": "service",
            "configuration_url": f"https://{self.coordinator.api.host}",
        }

    @property
    def should_poll(self):
        return False

    async def async_update(self):
        await self.coordinator.async_request_refresh()
