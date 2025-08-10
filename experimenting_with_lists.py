'''
In this script we're going to be experimenting with lists.
'''

from os import system
'''
# Define a list
names = ["Veronica","Rudie","Chris","Lorenzo","Gabs"]

print(names[3]) # Print one name from the list
print(names) # Print the whole list

# Define a list using variables
my_name = input("Enter your name: ")
system("clear")
mums_name = input("Input your mother's name: ")
system("clear")
dads_name = input("Input your father's name: ")
system("clear")

family = [my_name,mums_name,dads_name]

print(f"Your name is {family[0]}, your mum's name is {family[1]} and your dad's name is {family[2]}.")

print(f"There are {len(family)} people in your family.\n")

# Now use a loop and the option to append more people
group = []

friend = input("Name one of your friends: ").capitalize()
system("clear")

answer = "x"

while friend != "No":
    group.append(friend)
    friend = input("Name another of your friends: ").capitalize()
    system("clear")

system("clear")

print(f"Hey {my_name}, you have {len(group)} friends.")
print("Here they are:")
for friend in group:
    print(f"- {friend}")

input("\nPress any key to continue...")
system("clear")
'''
# Now to explore ways of manipulating lists

my_list = [] # define list

my_list.append("Gibson") # append one item
print(my_list)

my_list.insert(0,"Dan Electro") # insert items at specific positions
print(my_list)

my_list.extend(["Yamaha","Takamine","Harmony"]) # add multiple elemtents to a list using extend
print(my_list)

my_list.remove("Takamine") # remove Takamine from the list
print(my_list)

my_list.pop(1) # remove the second item in the list
print(my_list)

my_list.append(["old blood","ehx","boss","jam","faifield"]) # add a list within my_list using append
print(my_list)

print(my_list[1]) # print the second item in the list

print (my_list[3][2]) # print the third item in the list which is the fourth item of my_list

my_list.append(1+1) # appending a calculation to the list
print(my_list)
