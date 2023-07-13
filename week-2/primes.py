print("############################")
print("### PRIMES CHALLENGE ###")

def is_prime(number):
    if (number <= 1): 
        return False 
    for i in range(2,number): 
        if (number % i) == 0: 
            return False 
    return True

# create a list of integers from 2 - 1000
ints = list(range(2, 1001))
# create a new list of prime numbers
primes = [i for i, number in enumerate(ints) if is_prime(number)]

print(f"{len(primes)} primes. \nThe primes are: {primes}.")