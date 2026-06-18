# Function 1: Check if a single number is prime
def is_prime(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False
    
    # Check if any number from 2 up to num-1 can divide it evenly
    for i in range(2, num):
        if num % i == 0:
            return False  # Found a factor, so it is not prime
            
    return True  # No factors found, so it is prime

# Function 2: Print all prime numbers in a given range
def print_primes_in_range(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    
    # Loop through every number in the range
    for current_num in range(start, end + 1):
        # Call the first function to check the number
        if is_prime(current_num):
            print(current_num, end=" ")
    print()  # Print a new line at the end

# Example: Print prime numbers between 10 and 30
print_primes_in_range(10, 30)

