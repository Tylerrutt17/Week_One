anakin_mc_count = 20421
yoda_mc_count = 19699
c3p0_mc_count = 0

# is the midichlorian count greater than 20000. returns a true of false
print(anakin_mc_count > 20000)
print(anakin_mc_count < yoda_mc_count)

# basic stuff

name = ""
test = False

# false is always false, true is always true

if test == False: 
    name = "Jar Jar Binks"
else:
    print("True")

print("%s knows how to use a lightsaber" % name)

message = ""
print("Enter Star Wars Name!")
star_wars_name = input(message)
print("Welcome", star_wars_name, "to the Trade Federation!")