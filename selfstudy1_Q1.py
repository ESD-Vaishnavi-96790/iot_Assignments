# 1. Sample text to practice on
text = "  hello python world!  "

# 2. Changing the letter cases
print("--- Case Changes ---")
print("Original text:", text)
print("Upper case:", text.upper())  # Makes everything BIG
print("Title case:", text.title())  # Capitalizes first letter of each word

# 3. Cleaning up extra spaces
print("\n--- Cleaning Spaces ---")
cleaned_text = text.strip()
print("Stripped text (no side spaces):", cleaned_text)

# 4. Searching and replacing words
print("\n--- Search and Replace ---")
print("Starts with 'hello'?:", cleaned_text.startswith("hello"))
print("Replace 'world' with 'universe':", cleaned_text.replace("world", "universe"))

# 5. Splitting and joining text
print("\n--- Split and Join ---")
word_list = cleaned_text.split(" ")  # Cuts string into a list of words
print("Split into a list:", word_list)
print("Joined back with dashes:", "-".join(word_list))

