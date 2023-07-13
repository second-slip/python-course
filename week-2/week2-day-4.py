# Loops

# list comprehension
# newlist = [expression for item in iterable if condition == True]


# recap functions
def multiply_two_integers(num1, num2):
    return num1 * num2


result = multiply_two_integers(2, 2)
print(result)

# basic list
favourite_morrissey_songs = [
    "Suedehead",
    "The World Is Full of Crashing Bores",
    "The Youngest Was the Most Loved",
]

print(favourite_morrissey_songs)
# print an element by index
print(favourite_morrissey_songs[0])
# change one element by index
favourite_morrissey_songs[0] = "Spent the Day in Bed"
print(favourite_morrissey_songs)
# add an item with append
favourite_morrissey_songs.append("Istanbul")
print(favourite_morrissey_songs)

# pop default -1 / last element
favourite_morrissey_songs.pop()
print(favourite_morrissey_songs)

# pop access element by specific index
favourite_morrissey_songs.pop(1)
print(favourite_morrissey_songs)

# remove Removes the first item with the specified value
favourite_morrissey_songs.remove("The Youngest Was the Most Loved")
print(favourite_morrissey_songs)

# append method appends an element to the end of the list.
favourite_morrissey_songs.append("Istanbul")
favourite_morrissey_songs.append("Istanbul")
favourite_morrissey_songs.append("Istanbul")

# count() Returns the number of elements with the specified value
count = favourite_morrissey_songs.count("Istanbul")
print(count)

more_favourite_morrissey_songs = ["Forgive Someone", "Drag the River"]

# extend method adds the specified list elements (or any iterable) to the end of the current list.
favourite_morrissey_songs.extend(more_favourite_morrissey_songs)
print(favourite_morrissey_songs)

# insert dds an element at the specified position
favourite_morrissey_songs.insert(1, "That's How People Grow Up")
print(favourite_morrissey_songs)

# reverse()	Reverses the order of the list
favourite_morrissey_songs.reverse()
print(favourite_morrissey_songs)

# sort() method sorts the list ascending by default.
# can also make a function to decide the sorting criteria(s).
favourite_morrissey_songs.sort()
print(favourite_morrissey_songs)

# copy returns a copy of the list
copy = favourite_morrissey_songs.copy()
print(copy)

# index() returns the index of the first element with the specified value
index = favourite_morrissey_songs.index("Forgive Someone")
print(index)

# clear: removes all the elements
favourite_morrissey_songs.clear()
print(favourite_morrissey_songs)


print("############################")
print("### LOOPS ###")

# for x in list:
# for i in range(10)
# for i in range(1, 11)

# Activity(1):
# Create a list of 4 favourite films
# Use a for loop to show each film in the list
# Create a function called film_check() that checks if the
# 3rd film in the list is Ghostbusters.
# If it is, it should print “yey it’s ghostbusters”. If it isn’t, it
# should print “booo, we want ghostbusters”

films = [
    "Pokemon",
    "Jurassic Park",
    "Ghostbusters",
    "Super Mario"
]

# for film in films:
#     print(film)

def film_check(films):
    i = 0;
    for film in films:
        # print(film)
        if (film == "Ghostbusters") and (i == 2):
            print("yey it's ghostbusters");
        else:
            print("booo, we want ghostbusters")
        i += 1

film_check(films);


# Activity(2):
# If you can create a for loop to print 0
# 9 on the
# terminal, how can you create one to count
# backwards from 9 0?
# Consider the different ways we’ve used range and give
# it a go. Research if necessary!

for i in range(0, 10):
    print(i);

for i in range(9,0,-1):
    print(i);

print("######## WHILE LOOP")

i = 0

while i < 10:
    i += 1
    print(i);

import random;

rand = random.randint(0,50);
my_num = 37;
counter = 1;

print("Start")

while rand != my_num:
    rand = random.randint(0,50);
    counter += 1;
    print(rand);

print(f"{counter} times")

# Activity(1):
# Create a for loop that prints “hello world” 13
# times. Now, convert this into a while loop that
# does the same job.

# Activity(2):
# Create a variable, use a loop to generate a random
# number between 1 and 30 six times. For each
# random number generated, check if this number of
# divisible by 7 or not.

# Activity(3)
# Create a while loop to randomly cycle through a list of
# card suits until a given card suit is reached
# cards =
# [“Diamond”, “Spade”, “Club”, “
# Create a variable called
# current_card and use a list
# method to randomly give it a value from the list every
# time the loop runs. Then compare this to the suit you
# want to find to stop the while loop.

# Extra activity:
# Create a loop that asks a user to input a
# number, then displays the multiplication table
# for that number up to 12 e.g. if I input 1, I
# should see this
# Incorporate another loop so the program
# starts again and ask the user for a new
# number every time it finishes.





# print("############################")
# print("### PRIMES CHALLENGE ###")
def is_prime(number):
    if (number <= 1): 
        return False 
    for i in range(2,number): 
        if (number % i) == 0: 
            return False 
    return True 


# # create a list of integers from 2 - 1000
# ints = list(range(2, 1001))
# #print(ints)
# # create a new list of prime numbers
# primes = [i for i, number in enumerate(ints) if is_prime(number)]

# print(f"{len(primes)} primes. \nThe primes are: {primes}.")
