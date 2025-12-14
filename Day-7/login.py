#this is the script to login user

#importing getpass module to hide password input
#this get pass allow us to write the password without showing it on the screen and enhances security
import getpass  
correct_username = "admin"
correct_password = "password123"
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Login failed! Incorrect username or password.")

                        