import re

# Simple text to practice with
text = "The order ID is 123456 and the customer ID is 67890. Please call 555-1234 for help."


#=========== Part 1

print("=== PRACTICING re.search() ===")

# Example: Find the first digit in the text
first_digit = re.search(r"\d", text)
if first_digit:
    print(f"First digit: {first_digit.group()}")  # Should find: 1

# Task 1: Find the first word in the text
# hint: \w
first_word = re.search(r"\w+", text)
if first_word:
    print(f"First word: {first_word.group()}")

# Task 2: Find "555-1234" (the phone number)
# Hint: \d
phone = re.search(r"\d{3}-\d{4}", text)
if phone:
    print(f"Phone number: {phone.group()}")


#========== Part 2

print("\n=== PRACTICING re.findall() ===")

# Example: Find all single digits
all_digits = re.findall(r"\d", text)
print(f"All single digits: {all_digits}")  # Should find: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '5', '5', '5', '1', '2', '3', '4']

# Task 3: Find all complete numbers (one or more digits together)
# TODO: Use \d+ to find sequences of digits
all_numbers = re.findall(r"\d+", text)
print(f"All numbers: {all_numbers}")  # Should find: ['12345', '67890', '555', '1234']

# Task 4: Find all words
# TODO: Use \w+ to find all words
all_words = re.findall(r"\w+", text)
print(f"All words: {all_words}")

#=========== Part 3

print("\n=== PRACTICING EXACT COUNTS ===")

# Task 5: Find all 5-digit numbers (like the IDs)
# {n} qunatifier
five_digit_numbers = re.findall(r"\d{5}", text)
print(f"5-digit numbers: {five_digit_numbers}")  # Should find: ['12345', '67890']

# Task 6: Find all 3-digit numbers
#hint: {n} quantifier
three_digit_numbers = re.findall(r"\d{3}", text)
print(f"3-digit numbers: {three_digit_numbers}")  # Should find: ['123', '678', '555', '123']
