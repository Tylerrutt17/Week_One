
# #1
# name = input("what is your name?\n")
# #2
# print("Hello %s" % name)

# #3
# name = input("WHAT IS YOUR NAME?\n")
# print("HELLO", name)
# print("YOUR NAME HAS %s LETTERS IN IT" % len(name))

# #4
# print("I (name), am President of (Country)")
# mad_lib_input = input("Enter Your Name:\n")
# country_input = input("Enter any country name, fictional or not.\n")
# print("I %s, am President of %s" % (mad_lib_input, country_input))

# #5
# days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday, Sunday"]
# day_input = int(input("Enter a day of the week (number 0-6)\n"))
# print("Day Selected %s" % days_of_the_week[day_input])

# #6
# weekend_days = ["Sunday", "Saturday", "Friday"]
# weekend_day_input = int(input("Enter another day of the week. Work_or_sleep_in?\n"))
# if weekend_day_input >= 4:
#     print("It's a weekend Day!")
# else:
#     print("Get back to work!")

# #7
# celsius_input = int(input("Enter a temperature in celsius to convert to fahrenheit\n"))
# celsius_conversion = (celsius_input * 9/5) + 32
# print("Your Celsius to Fahrenheit Conversion -> %s" % celsius_conversion)

# #8
# incrementing_value = 0
# while incrementing_value < 10:
#     incrementing_value+=1
#     print("%d" % incrementing_value)

# #9
# starting_input = int(input("Enter number to start on\n"))
# ending_input = int(input("Choose a number to end on\n"))
# while starting_input < ending_input:
#     starting_input+=1
#     print(starting_input)

# #10
# square = "*****"
# starting_x_x = 0
# while starting_x_x < 5:
#     starting_x_x+=1
#     print(square)

# #11
# first_dimension_input = input("Enter the width of the square").upper

# TIp Calculator
# Your task is to write a program that calculates how much of a tip to leave at a restaurant.

# Prompt the user for two things:

# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%

try:
    total_bill_input = float(input("How Much was the bill?\n"))
except ValueError:
    print('You did not give a value error.')
    exit()

service_lvl = input("How was the service, (good, bad or fair)\n")
tip = 0.0

if service_lvl == "good":
    tip = total_bill_input * 0.2
elif service_lvl == "fair":
    tip = total_bill_input * 0.15
elif service_lvl == "bad":
    tip = total_bill_input * 0.1
    print(total_bill_input*0.10)
else:
    tip = float(input("enter specific tip amount\n"))

bill_plus_tip = tip + total_bill_input
print("Total Bill Amount = $%s" % bill_plus_tip)

round_up = input("Do You Want to Round your Bill up? (y or n)\n")
if round_up == "y":

elif round_up == "n":
    print("okay")
