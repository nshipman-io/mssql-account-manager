import os 
from argparse import ArgumentParser 

def create_parser(): 
    parser = ArgumentParser(description='Interact with a MS-SQL database via commandline')
    parser.add_argument('operation', choices=['reset','disable'])
    parser.add_argument('hostname', help='Hostname of the database you\'re connecting to.')
    parser.add_argument('database', help='Name of the database.')
    parser.add_argument('--port', '-p', default=1433, help='Port number to connect to MSSQL database. defaul is 1433')
    parser.add_argument('--user', '-u', help='Admin username to modify the database.')
    parser.add_argument('--password','-P', help='Password of the admin to authenticate.')

    return parser  

def main():
    from mssql import driver, users
    args = create_parser().parse_args()

    if args.user: 
        admin_username = args.user
    elif os.getenv("MSSQL_USER_NAME"):
        admin_username = os.getenv("MSSQL_USER_NAME")
    
    if args.password: 
        admin_password = args.password 
    elif os.getenv("MSSQL_PASSWORD"):
        admin_password = os.getenv("MSSQL_PASSWORD")
    
    if args.operation.lower() == 'reset':
        users.reset_password(driver.connect(args.hostname,admin_username,admin_password,args.database,args.port)
        ,str(input("Enter the user account to reset: ")))
        
    elif args.operation.lower() == 'disable':
        pass    
    
    
      