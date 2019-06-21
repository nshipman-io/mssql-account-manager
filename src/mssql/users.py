import sys
import random 
import string
import pymssql
from mssql import driver 

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(12, 16)
  return ''.join(random.choice(chars) for x in range(size))

def reset_password(connection,user_name):
    print("Generating random password and Altering Account")
    user_password = randompassword()
    cursor = connection.cursor()
    try:
        query=("""
        ALTER LOGIN %s WITH PASSWORD='%s' 
        """ % (user_name,user_password))
        cursor.execute(query)
        connection.commit()
        print(f"The new password for the user is {user_password}")
    except pymssql.ProgrammingError as err:
        print(f"Error: {err}") 
        print(f"Could not reset password for the user: {user_name}")
        sys.exit(1)
    print("Closing connection to database...")
    connection.close() 

def disable_user(connection,user_name): 
    print(f"Disabling user: {user_name}") 
    cursor = connection.cursor()
    try: 
      query=("""
      ALTER LOGIN %s DISABLE
      """ % (user_name)) 
      cursor.execute(query)
      connection.commit()
      print(f"User: {user_name} has been disabled.")
    except pymssql.ProgrammingError as err: 
      print(f"Error: {err}")
      print(f"Could not disable login for the user: {user_name}")
      sys.exit(1)
    print("Closing connection to database...")
    connection.close()
    
