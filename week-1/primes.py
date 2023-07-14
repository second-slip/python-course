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
    print(f"{len(primes)} primes found. \nThe prime numbers are: {primes}.")

print_primes_in_range(2, 1000) #(2,20)