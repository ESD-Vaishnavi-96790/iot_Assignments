def print_binary(number):
    # The bin() function changes a number to binary.
    # [2:] removes the '0b' from the start of the string.
    binary_format = bin(number)[2:]
    print(binary_format)


# Example usage:
print_binary(10)

