
'''
try:
    print(3/0)
except TypeError:
    print("Error")
'''
'''
 Create a program that asks for a number between 10 - 101. 
If the user enters anything that is not a number, or is less than 10 or greater than 101 throw some sort of insult.
If the number is 42 print a very positive message.
If the number -1 disregaurd the first point and print a message about being a smart person.
Any other print a message that includes the number given.


Create a program that ask for 2 numbers and then divides the first number from the second number.
Handle any possible errors without using any 'if'.
If the result is a valid option, print "The result is X" where X is the value.
Otherwise give an error that describes the issue.
(challange) Still without using if. Let the user know which value is causing and exemption.
(Extra Challange) Still without using ifs, If the first or second value is not a valid integer, have the program keep asking UNTIL the user supplies a valid integer. (think about the bolded word)   
'''

# try:
#     num1 = int(input("Enter first number\n"))
#     num2 = int(input("Enter second number\n"))
#     divide_num = num2 / num1
#     print("The Result is %s" % divide_num)
# except ValueError:
#     print("Error: Enter a number")
# except ZeroDivisionError:
#     print("Error: can't divide by zero")

# PROGRAM NUMBER 1
try:
    number = int(input("Enter a number between 10 - 101\n"))
    if number == -1:
        print("Clever!")
    elif number < 10 or number > 101:
        print("nice number")
    elif number == 42:
        print("VERY nice number")
    else: 
        print(number)
except ValueError:
    print("That\'s not a number")