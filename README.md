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

Useful links:
- [Get started with home assistant](https://www.home-assistant.io/installation/)
- [xStorage Home User Manual](https://www.eaton.com/content/dam/eaton/products/energy-storage/xstorage-home/en-gb/eaton-xstorage-home-user-interface-manual-en-gb.pdf)

---

### xStorage Home
1. Connect to the device's hotspot.
2. Access the local web UI: https://192.168.3.99. You will see an error in your browser, please click on the **advanced** button and proceed to visit the URL.
3. Select the link below the Sign in button **I am a technician**.
4. Login with the **admin** credentials as explained in the user manual above.
5. Navigate to **Unit Settings** and configure your internet source
6. Navigate back to the **General setting**, scroll down and locate the device IP address on the network interface you previously configured.
7. To make sure you got the right IP address, past it in your browser and you should be able to see the web UI again. If not, you did not use the proper IP address.
8. Save the IP address, you will need to enter it in the Home Assistant device configuration wizard.

---

### Home Assistant

#### Home Assistant Configuration
- Connect the home assistant gateway (device) to the local network where your xStorage Home is also connected
- [Click here to setup your device](http://homeassistant.local:8123)
- Update the software to the latest version

---

#### HACS Installation
HACS is an integration that will enable downloading the integration from xStorage Home. A GitHub account is required.
- [Click here to install the HACS integration](https://my.home-assistant.io/redirect/supervisor_addon/?addon=cb646a50_get&repository_url=https%3A%2F%2Fgithub.com%2Fhacs%2Faddons)

    ![Install](images/ha-open.png "Install HACS")

- Accept the download, when prompted

    ![Accept](images/get-hacs-install-confirmation.png "Accept HACS download")

- Install the Get HACS integration

    ![HACS Installed](images/hacs-install.png "Get HACS")

- Start the integration, by clicking on **start**

    ![Run](images/get-hacs-run.png "Run get HACS")

- Navigate to the log tab and make sure the download was completed.
- Restart your Home Assistant, navigate to **Settings** and use the more button (3 dots) on the top right corner:

    ![Restart](images/ha-restart.png "Home Assistant Restart")

- Clear your browser cache, while Home Assistant is restarting (login required after the operation). **This step is mandatory**.
- Navigate to **Settings** > **Devices & services**. In the bottom right corner, select **+ Add integration**.
- Search for HACS and click on the integration.

    ![Install HACS](images/hacs-install-integration.png "Install HACS")

- Accept all the disclaimers after carefully reading them.

    ![Disclaimer](images/hacs-disclaimer.png "Disclaimer")

- Device activation require that you follow the activation wizard on GitHub. Click on the link to proceed.

    ![Device Activation](images/hacs-github-code.png "Device Activation")

- Enter the device activation code from the previous page
    
    ![Activation code](images/hacs-configuration-device-activation.png "Enter your activation code")

- Click on **Continue**

    ![Continue](images/hacs-configuration-continue.png "Continue")

- Authorize HACS to access your GitHub account

    ![Restart](images/hacs-configuration-authorize.png "Home Assistant Restart")

- Congrats, you finished the HACS setup on GitHub!

    ![Success](images/github-wizard-success.png "Success")

- Select a zone to add to your HACS integration and click on **Finish**.

    ![Zone](images/hacs-configuration-final.png "Zone")

---

#### Eaton Battery Storage installation

- Navigate to **HACS** in the menu of your Home Assistant

    ![HACS](images/hacs-menu-link.png "Click on HACS")

- Use the top right 3 dots icon to add a custom repository.

    ![Add custom integration](images/hacs-link-custom-repository.png "Add custom integration")

- Enter the URL of the repository in the **Repository** field and select **Integration** as a type, then click on **Add**.

    ![Install Eaton Battery Storage](images/hacs-set-custom-repository.png "Install Eaton Battery Storage")

- Close the modal an look for the integration, by searching for **Eaton Battery Storage System**, click on the result and finally click on **Download** located on the bottom right corner of your browser.

- Navigate to **Settings** > **Devices & services**, then click on **Add integration** located on the bottom right corner of your browser.
- Type **Eaton Battery Storage System**, click on the result. Then enter the IP address of your **Eaton xStorage Home**, add the **API Key below** and hit submit.

    ![Configuration](images/integration-configuration.png "Configure the xStorage Home IP Address and API Key")

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJjb20uZWF0b24ueHN0b3JhZ2VIb21lIiwiY29tLnhzdG9yYWdlaG9tZS9zY28iOiJCQVNJQyIsImNvbS54c3RvcmFnZWhvbWUvY2lkIjoiNzNhZmRiNGRlODUwYjViMGY4YmIzZGQxNmVlNzMxNmY4YjkzZmJkZTUyNDMwY2YwZDhmODI5Yzc1NzdlIiwiaXNzIjoiaHR0cHM6Ly94c3RvcmFnZWhvbWUuY29tLyIsImNvbS54c3RvcmFnZWhvbWUvb3JnIjoiRWF0b24iLCJleHAiOjIwNjU2NTE3NzEsImlhdCI6MTc1MDA4MjI1MX0.ywwTNW1ofG9AMBWgQYsxXMV4lI_qFoOqyNSMIMg2o9lKWEgiW9Y4_I6pzZzwX5tJn9l7NsaF305JtK5IzuEZOuA1l_Ck0_8IxgS7YdXZROdK6QTh2qBp2PIMY68hFV5kejqoD3ZQThtzK9CHy07NSurNaCpMVtgAqQsFZc_Iwu7CbczeDb0KqPk4bJErdNaVXCw3YqsMAoz7Jp2L1AG26-0wwJzBGZd6HaOIxgw2m4LHDFY8UJ2jb1C0K_0g3m5b2HuzMZEecuNgM2IGFHAtw064jkWQUdrTKxdWgkKEq7DJhpeyBCNqUhBgYnk4YQEG_dYzSN8qN4SYxZC9tTH7TSqR-umYVw-0DaBrwobCF6f__WbzVpxBBEY7tQHeoOAYIlangf8dsQbPZkrAdMxC6RzPpjHBQBpvWFCid6bFcpSnNIaVnCCYvPClSs4p0BTBTmAdMMBq7f0SDBh52y9I90pqmX3PtQNzIWWcQTfe26lbTXubKVVY-4bRYRum-nem7qVNss6slS6crbjnYIR1pGe3fjA6KJAWTcYqljb4jwgEUCVTYVkzNr9Fn5JFFgeakW8U3cfWre6pMNLprQn_mRLLbiZQZjikK69O8bP1aC-M_CpLtJUtDRegQMgBJdJM-7LFUZtG-SWL0Gi0RUUGjaIHDlAETkDlK8tKzT7aufQ
```

> Congratulations, you should now have access to your **Eaton xStorage Home** metrics in Home Assistant