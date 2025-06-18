# Eaton Battery Storage for Home Assistant
Integrate your Eaton xStorage Home (Tiida) to home assistant with the local API.

## Pre-requisite
- A Home Assistant Gateway
- An Eaton xStorage Home (Tiida)
- A local network
- A GitHub account

Please make sure to setup all your devices on the same network.

Useful links:
- [Get started with home assistant](https://www.home-assistant.io/installation/)
- [xStorage Home User Manual](https://www.eaton.com/content/dam/eaton/products/energy-storage/xstorage-home/en-gb/eaton-xstorage-home-user-interface-manual-en-gb.pdf)

## Documentation

The available documentation provides 4 steps to setup an Eaton xStorage Hybrid unit with a Home Assistant device through local APIs.

- xStorage Home setup
- Setup Home Assistant
- HACS installation and configuration
- Eaton Battery Storage installation and configuration

<a href="https://greyfold.github.io/home_assistant_eaton_xstorage_home/" class="Button--primary Button--small Button">
    <span class="Button-content">
        <span class="Button-label">Read the documentation</span>
    </span>
</a>


## Available Metrics

All those metrics are provided by the xStorage Home API.

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