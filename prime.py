# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Taking input from the user
n = int(input("Enter a number: "))

# Checking if the number is prime
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
