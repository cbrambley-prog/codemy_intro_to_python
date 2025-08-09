
'''
This program is going to cover using variables in Python
'''

# First assign and print some variables
object = "Python"
print(object)

# Can I immediately redfine a variable?
object = "Bird"
print(object)

# Adding together variables
action = "Flight"

print(object + action) # concatenate using +

# Doing this within a string
print("Hey that's a long "+object+action) # using +
print(f"Hey that's a long {object+action}") # using an f string"

# Testing concatenation of different variable types
number = 4
# print(f"What is 4 + Bird... {number+object}") #}") # this errors because 4 is int and Bird in str
print(f"What is 4 + Bird... {str(number) + object}") # this will work because we convert variable 'number' to a string

print(f"What is 4 x Bird... {number*object}") # multiply a string by x to repeat the string x times

'''
Now we're going to look at assignment operators
'''
print("\nPrint a couple of new lines to space things out\n") # printing new lines

num_1 = 3

# Assign
num_2 = num_1
print(f"num_1 = 3. Set num_2 = num_1: num_2 = {num_2}")

# Add and assign
num_2 += num_2
print(f"Add and assign num_2 to itself: num_2 += num_2 = {num_2}")

# Subtract and assign
num_2 -= 4
print(f"Subtract and assign 4 to num_2: num_2 -= 4 = {num_2}")

# Multiply and assign
num_2 *= 15
print(f"Multiply and assign 3 to num_2: num_2 *= 15 = {num_2}")

# Divide and assign
num_2 /= 2
print(f"Divide and assign 2 to num_2: num_2 /= 2 = {num_2}")

# Modulus and assign
num_2 %= 4
print(f"Modulus and assign 4 to num_2: num_2 %= 10 = {num_2}")

'''
Now we're going to play with user input
'''

name = input("What's your name? ")
instrument = input("What's your favorite instrument? ")
quantity = int(input(f"How many {instrument}s would you like, {name}? "))

quantity += 1
print(f"Awesome. Here's {quantity} {instrument.lower()}s {name}, I threw in a free one because you're cool.")
