# Loops

# list comprehension
# newlist = [expression for item in iterable if condition == True]

print("############################")
print("### LOOPS ###")




for i in range(0, 10):
    print(i)

for i in range(9, 0, -1):
    print(i)

print("######## WHILE LOOP")

i = 0

while i < 10:
    i += 1
    print(i)

import random

rand = random.randint(0, 50)
my_num = 37
counter = 1

print("Start")

while rand != my_num:
    rand = random.randint(0, 50)
    counter += 1
    print(rand)

print(f"{counter} times")

