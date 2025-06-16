# Eaton Battery Storage for Home Assistant
Integrate your Eaton xStorage Home (Tiida) to home assistant with the local API.

## Available Metrics

| Metric       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `temp`       | Inverter temperature (°C)                                                   |
| `etoday`     | Energy produced today (Wh or kWh, depending on system)                      |
| `vbat`       | Battery voltage (V)                                                         |
| `ibat`       | Battery current (A)                                                         |
| `mtf`        | Minutes to full charge (min)                                                |
| `vpv1`       | PV1 voltage (V)                                                             |
| `ipv1`       | PV1 current (A)                                                             |
| `iac`        | Inverter AC output current (A)                                              |
| `fac`        | Inverter output frequency (Hz)                                              |
| `pac`        | Inverter output power (W)                                                   |
| `pload`      | Power consumed by critical loads (W)                                        |
| `etotal`     | Total energy produced (Wh or kWh)                                           |
| `htotal`     | Total operating hours                                                       |
| `edraw`      | Energy drawn from the grid (Wh or kWh)                                      |
| `grid_code`  | Grid configuration code (region-specific settings)                          |
| `vbus`       | DC bus voltage (V)                                                          |
| `vpv2`       | PV2 voltage (V) (if supported by firmware)                                  |
| `ipv2`       | PV2 current (A) (if supported by firmware)                                  |

## Setup instructions

### Pre-requisite
- A Home Assistant Gateway
- An Eaton xStorage Home (Tiida)
- A local network

Please make sure to setup all your devices on the same network.

Get started with home assistant: https://www.home-assistant.io/installation/

xStorage Home User Manual: https://www.eaton.com/content/dam/eaton/products/energy-storage/xstorage-home/en-gb/eaton-xstorage-home-user-interface-manual-en-gb.pdf

### xStorage Home Configuration
1. Connect to the device's hotspot.
2. Access the local web UI: https://192.168.3.99. You will see an error in your browser, please click on the **advanced** button and proceed to visit the URL.
3. Select the link below the Sign in button **I am a technician**.
4. Login with the **admin** credentials as explained in the user manual above.
5. Navigate to **Unit Settings** and configure your internet source
6. Navigate back to the **General setting**, scroll down and locate the device IP address on the network interface you previously configured.
7. To make sure you got the right IP address, past it in your browser and you should be able to see the web UI again. If not, you did not use the proper IP address.
8. Save the IP address, you will need to enter it in the Home Assistant device configuration wizard.

### Home Assistant Configuration
1. Connect the home assistant gateway (device) to the local network where your xStorage Home is also connected
2. Setup your device or login on http://homeassistant.local:8123
3. Navigate to **settings** > **Additional plugins**
4. Search for HACS and install it
5. In HACS, add a custom extension
6. Enter the URL of this extension https://github.com/myearth-ch/home_assistant_eaton_xstorage_home
7. When installed, navigate to **settings** > **Device ....**
8. Click on the add integration button and search for Eaton xStorage Home
9. Enter the IP address of your xStorage Home
