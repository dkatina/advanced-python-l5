#Character sets allow us to create our own metacharacters, to specify what we are looking for

import re

#Character sets use square brackets [whatever characters we want]

text = "Product codes: A123, B456, C789, X999, a111"

#grabbing codes with \w
codes = re.findall(r"\w+", text)
print(codes)

#Using a character set we can refine our search
specific_codes = re.findall(r'[ABC]\d{3}',text)
print(specific_codes)

#Create a range of characters A-Z
code_pattern = re.findall(r'[A-Z]\d{3}', text)
print(code_pattern)

#Include all abc characters regardless of casing: A-Za-z shorthand: A-z (all abc characters)
casing_code_patterns = re.findall(r'[A-z]\d{3}', text)
print(casing_code_patterns)

#Target on abc words
words = re.findall(r'[A-z]+', text)
print(words)

#Number ranges [0-9] behaves like \d
numbers = re.findall(r'[0-9]+',text)
print(numbers)

#Partial number range [0-5]
low_nums = re.findall(r'[0-5]\d+', text)
print(low_nums)

#==================== Common Character Sets =====================

phone_data = "Call 555-123-4567 or (999)-888-7777"

digits = re.findall(r"[0-9()-]+", phone_data)
print(digits)

# includes: abc, nums, - , _, ., +
# followed by @
# followed: abc, _
# followed by: 2-3 char extensions

email = re.compile(r'["A-z0-9-_+.]+@[A-z_-]+\.[A-z]{2,3}')

my_email = "dylank@codingtemple.com"

email_match = email.search(my_email)
print(email_match.group())