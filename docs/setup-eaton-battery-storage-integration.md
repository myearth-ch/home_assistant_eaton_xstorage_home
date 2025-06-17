# Eaton Battery Storage installation

- Navigate to **HACS** in the menu of your Home Assistant

    ![HACS](https://github.com/myearth-ch/home_assistant_eaton_xstorage_home/blob/main/images/hacs-menu-link.png "Click on HACS")

- Use the top right 3 dots icon to add a custom repository.

    ![Add custom integration](https://github.com/myearth-ch/home_assistant_eaton_xstorage_home/blob/main/images/hacs-link-custom-repository.png "Add custom integration")

- Enter the URL of the repository in the **Repository** field and select **Integration** as a type, then click on **Add**.

    ![Install Eaton Battery Storage](https://github.com/myearth-ch/home_assistant_eaton_xstorage_home/blob/main/images/hacs-set-custom-repository.png "Install Eaton Battery Storage")

- Close the modal an look for the integration, by searching for **Eaton Battery Storage System**, click on the result and finally click on **Download** located on the bottom right corner of your browser.

- Navigate to **Settings** > **Devices & services**, then click on **Add integration** located on the bottom right corner of your browser.
- Type **Eaton Battery Storage System**, click on the result. Then enter the IP address of your **Eaton xStorage Home**, add the **API Key below** and hit submit.

    ![Configuration](https://github.com/myearth-ch/home_assistant_eaton_xstorage_home/blob/main/images/integration-configuration.png "Configure the xStorage Home IP Address and API Key")

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJjb20uZWF0b24ueHN0b3JhZ2VIb21lIiwiY29tLnhzdG9yYWdlaG9tZS9zY28iOiJCQVNJQyIsImNvbS54c3RvcmFnZWhvbWUvY2lkIjoiNzNhZmRiNGRlODUwYjViMGY4YmIzZGQxNmVlNzMxNmY4YjkzZmJkZTUyNDMwY2YwZDhmODI5Yzc1NzdlIiwiaXNzIjoiaHR0cHM6Ly94c3RvcmFnZWhvbWUuY29tLyIsImNvbS54c3RvcmFnZWhvbWUvb3JnIjoiRWF0b24iLCJleHAiOjIwNjU2NTE3NzEsImlhdCI6MTc1MDA4MjI1MX0.ywwTNW1ofG9AMBWgQYsxXMV4lI_qFoOqyNSMIMg2o9lKWEgiW9Y4_I6pzZzwX5tJn9l7NsaF305JtK5IzuEZOuA1l_Ck0_8IxgS7YdXZROdK6QTh2qBp2PIMY68hFV5kejqoD3ZQThtzK9CHy07NSurNaCpMVtgAqQsFZc_Iwu7CbczeDb0KqPk4bJErdNaVXCw3YqsMAoz7Jp2L1AG26-0wwJzBGZd6HaOIxgw2m4LHDFY8UJ2jb1C0K_0g3m5b2HuzMZEecuNgM2IGFHAtw064jkWQUdrTKxdWgkKEq7DJhpeyBCNqUhBgYnk4YQEG_dYzSN8qN4SYxZC9tTH7TSqR-umYVw-0DaBrwobCF6f__WbzVpxBBEY7tQHeoOAYIlangf8dsQbPZkrAdMxC6RzPpjHBQBpvWFCid6bFcpSnNIaVnCCYvPClSs4p0BTBTmAdMMBq7f0SDBh52y9I90pqmX3PtQNzIWWcQTfe26lbTXubKVVY-4bRYRum-nem7qVNss6slS6crbjnYIR1pGe3fjA6KJAWTcYqljb4jwgEUCVTYVkzNr9Fn5JFFgeakW8U3cfWre6pMNLprQn_mRLLbiZQZjikK69O8bP1aC-M_CpLtJUtDRegQMgBJdJM-7LFUZtG-SWL0Gi0RUUGjaIHDlAETkDlK8tKzT7aufQ
```

> Congratulations, you should now have access to your **Eaton xStorage Home** metrics in Home Assistant