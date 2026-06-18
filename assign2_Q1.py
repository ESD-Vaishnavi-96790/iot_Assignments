def count_vowels(text):
    # This function counts the total number of vowels.
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def count_consonants(text):
    # This function counts letters that are not vowels.
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        # .isalpha() ensures we only count real alphabet letters, not numbers or spaces.
        if char.isalpha() and char not in vowels:
            count += 1
    return count


def calculate_ratio(v_count, c_count):
    # This function divides vowels by consonants.
    if c_count == 0:
        return "Undefined (Cannot divide by zero consonants)"
    return v_count / c_count


# --- Main Program Logic ---
# 1. Get input text from the user
user_string = input("Enter a string: ")

# 2. Call the counting functions
num_vowels = count_vowels(user_string)
num_consonants = count_consonants(user_string)

# 3. Calculate the final math ratio
vowel_consonant_ratio = calculate_ratio(num_vowels, num_consonants)

# 4. Show the results
print(f"Number of Vowels: {num_vowels}")
print(f"Number of Consonants: {num_consonants}")
print(f"Ratio of Vowels to Consonants: {vowel_consonant_ratio}")

