def print_fibonacci(terms):
    # Step 1: Handle cases where the user asks for 0 or negative terms
    if terms <= 0:
        print("Please enter a number greater than 0.")
        return
    
    # Step 2: Set up the first two numbers of the series
    n1, n2 = 0, 1
    count = 0
    
    print("Fibonacci series:")
    
    # Step 3: Loop until we print the requested number of terms
    while count < terms:
        print(n1, end=" ")
        # Find the next number by adding the last two
        next_num = n1 + n2
        # Update the numbers for the next turn
        n1 = n2
        n2 = next_num
        count += 1
    print()  # Print a new line at the end

# Example: Print the first 7 terms
print_fibonacci(7)

