import random

# Activity(1):
# Create a for loop that prints “hello world” 13
# times. Now, convert this into a while loop that
# does the same job.

for i in range(0, 13):
    print("hello world")

while i < 10:
    print("hello world")

# Activity(2):
# Create a variable, use a loop to generate a random
# number between 1 and 30 six times. For each
# random number generated, check if this number of
# divisible by 7 or not.

def print_is_div_by_7():
    randomNum = random.randint(1, 30)

    if randomNum % 7 == 0:
        print(f"{randomNum} is divisable by 7")
    else:
        print(f"{randomNum} is NOT divisable by 7")


for i in range(0, 6): 
    print_is_div_by_7()


# Activity(3)
# Create a while loop to randomly cycle through a list of
# card suits until a given card suit is reached
# cards =
# [“Diamond”, “Spade”, “Club”, “
# Create a variable called current_card and use a list
# method to randomly give it a value from the list every
# time the loop runs. Then compare this to the suit you
# want to find to stop the while loop.
cards = ["Diamond", "Spade", "Club", "Heart"]
current_card = ""

i = 0
while current_card != "Club":
    rand = random.randint(0, 3)
    current_card = cards[rand]
    print(current_card)
    i += 1

print(f"{i} times")


# Extra activity:
# Create a loop that asks a user to input a
# number, then displays the multiplication table
# for that number up to 12 e.g. if I input 1, I
# should see this
# Incorporate another loop so the program
# starts again and ask the user for a new
# number every time it finishes.
def multiply(num1, num2):
    return num1 * num2;

def printer(num1, num2, num3):
    print(f"{num1} x {num2} = {num3}")

def create_multiplication_table(number):
    for i in range(1, 13):
        result = multiply(i,number);
        printer(number, i, result)

print('Input a number to print its multiplication table:')
x = input()
x = int(x)
create_multiplication_table(x);



# Extra activity (DIFFICULT):
# Create a program that checks whether all numbers
# between 1 and 20 are prime numbers or not.

print("############################")
print("### PRIMES CHALLENGE ###")

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True

def print_primes_in_range(start, end):
    # guards: start < end, etc?
    primes = [i for i in range(start, end) if is_prime(i)]
    print(f"{len(primes)} primes found in range {start} - {end}. \nThe prime numbers are: {primes}.")

print_primes_in_range(2, 1000)

