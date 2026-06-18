# Step 1: Ask the user to enter a 5-digit number
user_input = input("Enter a 5-digit number: ")

# Step 2: Reverse the input
reversed_input = user_input[::-1]

# Step 3: Check if the original number matches the reversed number
if user_input == reversed_input:
    print("Yes, it is a numeric palindrome!")
else:
    print("No, it is not a numeric palindrome.")

