import random 
import string
import pymssql
from mssql import driver 

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(8, 12)
  return ''.join(random.choice(chars) for x in range(size))

def reset_password(connection,user_name):
    print("Generating random password and Altering Account")
    user_password = randompassword()
    cursor = connection.cursor()
    try:
        query=("""
        ALTER LOGIN %s WITH PASSWORD='%s' 
        """ % (user_name,user_password))
        print(query)
        cursor.execute(query)
        connection.commit()
        print(f"The new password for the user is {user_password}")
    except pymssql.ProgrammingError as err:
        print(f"Error: {err}") 
        print(f"Could not reset password for the user: {user_name}")
    print("Closing connection to database...")
    connection.close()
    