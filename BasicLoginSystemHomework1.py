#Homework1 - Login System
#Initial variables
age = int(input("How old are you: "))
username = input("Create Username: ")
password = input("Create Password: ")

#Attempt Variables
username_attempt = input("Enter Username: ")
password_attempt = input("Enter Password: ")

#a function that checks if the user is old enough to get full access
def age_function(age):
    if age >= 13:
       print("with full access")
    else:
        print("with partial access")

#if the user correctly enters username and password allow them to login if not they fail
if username_attempt == username and password_attempt == password:
    print("Successfully logged in ")
    #if the user is older than 13 give full access if not give partial access
    age_function(age)

else: #if the username or password are incorrect
    print("Unable to login")
    