MSSQL-ACCOUNT-MANAGER
===================== 
CLI tool for managing user account and reporting for Microsoft SQL Server. 

Preparing the Development 
-------------------------
1. Ensure `pip` and `pipenv` are installed. 
2. `cd` into the repository. 
3. Fetch development dependencies `make install` 
4. Activate virtualenv: `pipenv shell` 
5. Create the package `python setup.py bdist_wheel`

Installation
------------ 
1. `cd` into the directory `mssql-account-manager`
2. `pip3 install dist/mssql_account_manager-0.1.0-py3-none-any.whl ` 

Usage 
-----
Base Example: 
::
    `mssqlam reset <hostname> <db_table> --user <admin_user> --password <admin_password>`

Ports: 
::
    `mssqlam reset <hostname> <db_table> --user <admin_user> --password <admin_password> --port 11433`

Uninstall
---------
1. `cd` into the directory `mssql-account-manager`
2. `pip3 uninstall dist/mssql_account_manager-0.1.0-py3-none-any.whl`