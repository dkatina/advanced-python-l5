import re

text = "Contact us at info@company.com or call 555-0123"

#using re.search() - to find the first instance of our pattern

#================ Metacharacters ================

#\d - Find any digit (0-9)
single_digit = re.search(r"\d", text)
print(single_digit.group()) #Returns 5 since this is our first single digit

#\w - finds any word character (letters, digits, underscores)
word_match = re.search(r"\w", text)
print(word_match.group())

#\s - Finds any whitespace (spaces, tabs, newlines)
white_space_match = re.search(r'\s', text)
print(white_space_match.start()) #returns 7, index of the first space

# . - Wildcard that will return ANY character
any_char_match = re.search(r".", text)
print(any_char_match.group())

#=============== Quantifiers ========================

#============= + means "one or more" 
#find running digits
# \d+ 
first_nums = re.search(r"\d+", text)
print(first_nums.group())

#findall() - return a list of all instances of text that match our pattern.
all_nums = re.findall(r"\d+", text)
print(all_nums)

words = "The cat could run as fast as the dog could, it's not a fascad. 00d"

#\w+: what do we expect to get when we .findall()
all_words = re.findall(r'\w+', words)
print(all_words)

#Looking for 0g
words_and_numbers = re.findall(r'\d+\w', words)
print(words_and_numbers)

# c\w+ : What kind of pattern does this create?
c_words = re.findall(r"\sc\w+", words)
print(c_words)

# ================ * "0 or more"

# ================ ? "0 or 1" is or isn't there

# ================ {n} "exactly n times"

text = "Contact us at info@company.com or call 423-555-0123"

# Find digits that repeat exactly three times
three_digits = re.findall(r"\d{3}", text)
print(three_digits)

#Find last four digits in the phone number
last_four = re.findall(r"\d{4}", text)
print(last_four)

# ================ {n,m} "Between n and m repeats"

id_text = "Employees: ID001, ID45, ID12345, ID7"
long_ids = re.findall(r'\w{2}\d{3,5}', id_text)
print(long_ids)


periods = "a text . with periods ."
found = re.findall(r"\.", periods) # \ removes the power from quantifiers, and metacharacters

print(found)

