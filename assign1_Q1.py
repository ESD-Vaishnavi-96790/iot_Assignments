# Step 1: Get the first number from the user
num1 = float(input("Enter the first number (numerator): "))

# Step 2: Get the second number from the user
num2 = float(input("Enter the second number (denominator): "))

# Step 3: Check if the second number is zero
if num2 == 0:
    print("Error: You cannot divide by zero!")
else:
    result = num1 / num2
    print(f"The result of the division is: {result}")

