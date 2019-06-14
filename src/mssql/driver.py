import pymssql

def connect(hostname,user,password,database,port):
    print(f"Connectiong to the instance: {hostname}")
    conn = pymssql.connect(
        server=hostname,
        user=user,
        password=password,
        database=database, 
        port=port)
    return conn