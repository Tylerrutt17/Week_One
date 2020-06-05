# coin_count = 0
# print("You have 0 Coins?")
# while True:
#     count_input = input("Do you want a coin? y or n\n")
#     if count_input == "y":
#         coin_count+=1
#         print("You now have %s coins's" % coin_count)
#     elif count_input == "n":
#         print("Okay, bye")
#         break
#     else:
#         print("Not a valid input, try again.")


# # printing a box
# x_dimension_input = int(input("Enter the size in width of your box\n"))
# y_dimension_input = int(input("Enter the size in height of your box\n"))

# increment = 0
# y_dimension = y_dimension_input

# star_string = ""

# for x in range(0, y_dimension):
#     if x == 0:
#         for star in (0, x_dimension_input):
#             star_string+= "*"
#             if star == x_dimension_input:
#                 print(star_string)



from random import randrange
import random

while True:
    low_range_int = int(input("Enter the low range value\n"))
    high_range_int = int(input("Enter the high range value\n"))
    # selecting a random number based off of the integers the user entered.
    random_number = random.randint(low_range_int, high_range_int)
    GUESSES_LEFT = 5

    print("I, the computer, am thinking of a number between %d-%d" % (low_range_int, high_range_int))

    while True:
        try:
            your_guess_input = int(input("Whats the number?\n\n"))
            if your_guess_input == random_number:
                print("\nYou Got it")
                break
            elif your_guess_input != random_number:
                GUESSES_LEFT+= -1
                if GUESSES_LEFT > 0:
                    if your_guess_input > random_number:
                        print("\nToo High")
                    else:
                        print("\nToo Low")
                    print("%d Guesses Left" % GUESSES_LEFT)
                else:
                    print("Oops, your just bad at this game...Ran out of guesses")
                    break
        except ValueError:
            print("ERROR: Please Enter a Integer")


    play_again_input = input("Do you want to play again? (y or n)\n")
    if play_again_input == "y":
        continue
    else:
        print("Thanks for playing!")
        break


# Create a program that lists your top 3 favorite foods.
# You can only write a single print statement.
# The list must have at least 5 items.
# Create a program that prints out the results from a list.
# You can only have one viarable in the whole program
# It can only be on two lines

# #1
# favorite_foods = ["Pizza", "Salmon", "Chicken", "Tacos", "Burgers"]
# for food in favorite_foods:
#     print(food)

# #2
# print(favorite_foods[0:5])


# Create a program that prints the ingredients of your 3 favorite foods. 
# 1. The ingredients must be in a list inside of the foods list
# 2. Before each food print "Food # X has the following ingredients". Where X is the index of the food.
# 3. (Challange) You can only use the for in operation.
# 4. (Extra Challenge) Make it a quiz game of guess the food based on its ingredients. Add more food items if needed.

# food_names = ["pizza", "burger", "seafood"]
# pizza = ["Dough", "Sauce", "Cheese"]
# burger = ["Beef", "Cheese", "Bun"]
# seafood = ["Crab", "Shrimp", "Salmon"]
# fav_foods = [pizza, burger, seafood]
    
# for index, food in enumerate(fav_foods):
#     print("\nFood %s has the following ingredients" % index)
#     for ingredient in food:
#         print(ingredient)

#     guess = input("\nGuess what food type item #%s is\n" % index)
#     if guess == food_names[index]:
#         print("You Got It! Here's the next one")
#     else:
#         print("You Missed It...")
    
# print("\n")

# numbers_1 = [2, 4, 5]
# numbers_2 = [2, 3, 6]
# multiplied_list = []

# for index, number1 in enumerate(numbers_1):
#     number2 = numbers_2[index]
#     # New number made by multiplying item from numbers_1[index] with number_2[index] // At same Index
#     multiplied_number = number2 * number1
#     multiplied_list.append(multiplied_number)
# print("New Multiplied Numbers List %s" % multiplied_list)


# #NOT SURE WHAT THE MATRIX ADDITION MEANS

# # De-dup
# list_1 = [1, 3, 5, 7, 9, 9, 9, 6, 7, 7]
# # Creates a dictionary using the list items as the keys. Removes the duplicates because dictionaries cannot have duplicate keys
# duplicates_removed_list = list(dict.fromkeys(list_1))
# print("Duplicates removed -> %s" % duplicates_removed_list)

# # Leek Speak
# leek_dictionary = {"A": "4", "B": "13", "C": "()", "D": "[)", "E": "3", "F": "|=", "G": "6", "H": "|-|", "I": "|", "J": ".]", "K": "|<", "L": "1", "M": "|Y|", "N": "/\/", "O": "0", "P": "|>", "Q": "0,", "R": "|2", "S": "5", "T": "7", "U": "[_]", "V": "\/", "W": "\ v /", "X": "}{", "Y": "'/", "Z": "2"}
# dic_index = list(leek_dictionary.keys()).index("C")
# print(dic_index)

# translated_string = input("Please Enter your string to be translated to Leek Speak\n")
# uppercased_entry = translated_string.upper

# for character in uppercased_entry:
#     print(character)











