import sys
import pymssql

def connect(hostname,user,password,database,port):
    try:
        print(f"Connecting to the instance: {hostname}")
        conn = pymssql.connect(
            server=hostname,
            user=user,
            password=password,
            database=database, 
            port=port)
    except pymssql.OperationalError as err:
        print(f"Error: {err}")
        sys.exit(1)
    return conn