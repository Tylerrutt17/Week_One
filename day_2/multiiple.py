#Create a program that will ask for a username and then a password.
#If the username or password length is less than 6 charecters give a too short message.
#if the username or password length is greater than 12 charecters give a too long message
#Have the user confirm the password in again.
#If the passwords match give a sucess message
#if the passwords do not match give a mismatch message
#If the password is only numbers give a message that says it cannot be a number.
#(challange) have only one print statement in the whole program.

'''

username = input("Enter Username!\n")
password = input("Enter Password\n")

# Checking if the username or password are shorter than 6 characters
if len(username) < 6 or len(password) < 6:
    print("Password or username is too short")
# Checking if the username or password are longer than 12 characters
elif len(username) > 12 or len(password) > 12:
    print("Password or username is too long") 
else:
    confirm_password = input("Please confirm password\n")
    if confirm_password == password:
        if confirm_password.isdigit:
            print("Can't Use A Number in your password")
        else:
            print("Success, password confirmed")
    else:
        print("Passwords are different")

'''

# Programming loops
'''
Create a program that prints 1 - 10 using a while loop.
Print a seperator like '-----' in between each number.
Create a program that counts down from 100 to 0 by 10s.
Each line needs to print "D% downloaded R% remaining. Where D is the current curent value  divided by 100 and R is the current value.
Skip 50 and 30. (Do not print thoses) 
'''

decrementedvalue = 100

while decrementedvalue > 0:
    if decrementedvalue != 50 and decrementedvalue != 30:
        print("----%d%% downloaded ----%r%% remaining" % (decrementedvalue - 100, decrementedvalue))
    decrementedvalue-= 10.0
    