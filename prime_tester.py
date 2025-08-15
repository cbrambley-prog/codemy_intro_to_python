'''
The purpose of this script is to identify if a number is prime, and return a true or false respone.
'''
from os import system

'''
# check the integer test
num1 = float(input("Enter a number: "))
print(num1.is_integer())

system("clear")
'''

'''
print("We will test whether a number is prime or not.")
num2 = int(input("Input a integer (non-zero): "))

not_prime = 0

for i in range(2,num2-1):
    if num2/i == int(num2/i):
        print(f"{i}")
        print(f"{num2/i}")
        print(f"{num2} is not a prime number.")
        not_prime = 1
        break # if we find a number that divides num2 to an integer, break the loop

if not_prime == 0:
    print(f"{num2} is a prime number.")
'''

'''
1. Work on an example myself/2. Write down what I did.
Unsure of definition of prime number, so googled it:
a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1

Start with 2. 2 only divides by itself and 1, so isn't prime.

3? 3/2 = 1.5. Prime.
4? 4/2 = 2, not prime.

3. Generalise
Take number, interate from 2 to that number -1.
If at any point the number divides by the iterator to give an interger, it's not prime.
If we reach the end of the sequence with no integer, write it down as prime.
Move to our number + 1 and repeat.
Stop when we have the number of prime numbers we wanted.
'''

how_many = float(input("This will print the first x prime numbers, enter x as an integer: "))
prime = "y"
primes = 0
check_for_prime = 2

while primes < how_many:
    prime = "y"
    check_for_prime += 1

    for i in range(2,check_for_prime-1):
        if check_for_prime/i == int(check_for_prime/i):
            prime = "n"
            break
    
    if prime == "y":
        primes += 1
        print(check_for_prime)