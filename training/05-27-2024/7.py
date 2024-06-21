def is_prime(n):
# function to find prime or not.
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(num):
#Function to find the next prime number.
    if num <= 1:
        return 2
    prime = num
    found = False
    while not found:
        prime += 1
        if is_prime(prime):
            found = True
    return prime

# Input a number
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
    print("The number", num, "is prime.")
else:
    print("The number", num, "is not prime.")
    next_prime_num = next_prime(num)
    print("The next prime number is:", next_prime_num)
