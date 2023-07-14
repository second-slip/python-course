import datetime;

next_birthday = datetime.datetime(2024, 4, 21);
today = datetime.datetime.now();
days_to_next_birthday = next_birthday - today;

print(f"{days_to_next_birthday.days} until my next birthday.");


import random;
print(random.random()); # float in range 0-1
print(random.randint(1, 10)); # integer in range 1 - 10
print(random.uniform(1,10)); # float in given range

from random import random, randint, uniform
print(random()); # float in range 0-1
print(randint(1, 10)); # integer in range 1 - 10
print(uniform(1,10)); # float in given range

a = 5;
b = 2;
a *= b;
print(a);

a ="hello";
b = " there";
c = a + b;
print(c);

# = (simple assignment)
# Assigns a value to a variable(s)

# += (increment assignment)
# Adds a value and the variable and assigns the result to that variable.

# -= (decrement assignment)
# Subtracts a value from the variable and assigns the result to that variable.

# *= (multiplication assignment)
# Multiplies the variable by a value and assigns the result to that variable.

# /= (division assignment)
# Divides the variable by a value and assigns the result to that variable.

# **= (power assignment)
# Raises the variable to a specified power and assigns the result to the variable.

# %= (modulus assignment)
# Computes the modulus of the variable and a value and assigns the result to that variable.

# //= (floor division assignment)
# Floor divides the variable by a value and assigns the result to that variable.