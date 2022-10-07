#Password authentication system using python
import getpass #getpass is used to make sure that password user is entering is hidden
database={"arjun":"arjun","karthik":"karthik"}
username=input('Enter the username: ')
password=getpass.getpass('Enter the password: ')
for i in database.keys():
    if(username==i):
        while password!=database.get(i):
            password=getpass.getpass('Enter the password again: ')
        break
print('Verified')