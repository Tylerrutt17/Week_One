#Create a program that asks for a name and if the name is your name print "You May Enter", otherwise print "Get Out"
#Anything printed must be a variable.

print("Please Enter Your Name")

message = ""
name = input(message)

if name == "Tyler":
    print("You May Enter")
else:
    print("get out!")

#Create a Program that ask for an age if the age is older than 21 print "You may enter" otherwise print "Get Out"
#Test it with a letter instead of a number... and then speak up in chat what happens.

agetest = 0
age = input(agetest)
if int(age) > 21:
    print("You May Enter")
else:
    print("Get Out")