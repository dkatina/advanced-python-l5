# Lesson 5: Regular Expressions - Student Assignments

## Assignment 1: Practicing Basic Patterns

### Scenario
Practice using the regex concepts you just learned! Start simple and build confidence with `re.search()`, `re.findall()`, and basic patterns.


### The Dataset
```python
import re

# Simple text to practice with
text = "The order ID is 12345 and the customer ID is 67890. Please call 555-1234 for help."
```

### Your Tasks

#### Part 1: Practicing re.search()

```python
print("=== PRACTICING re.search() ===")

# Example: Find the first digit in the text
first_digit = re.search(r"\d", text)
if first_digit:
    print(f"First digit: {first_digit.group()}")  # Should find: 1

# Task 1: Find the first word in the text
# hint: \w
first_word = re.search(r"# YOUR PATTERN HERE", text)
if first_word:
    print(f"First word: {first_word.group()}")

# Task 2: Find "555-1234" (the phone number)
# Hint: \d
phone = re.search(r"# YOUR PATTERN HERE", text)
if phone:
    print(f"Phone number: {phone.group()}")
```

#### Part 2: Practicing re.findall()

```python
print("\n=== PRACTICING re.findall() ===")

# Example: Find all single digits
all_digits = re.findall(r"\d", text)
print(f"All single digits: {all_digits}")  # Should find: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '5', '5', '5', '1', '2', '3', '4']

# Task 3: Find all complete numbers (one or more digits together)
# TODO: Use \d+ to find sequences of digits
all_numbers = re.findall(r"# YOUR PATTERN HERE", text)
print(f"All numbers: {all_numbers}")  # Should find: ['12345', '67890', '555', '1234']

# Task 4: Find all words
# TODO: Use \w+ to find all words
all_words = re.findall(r"# YOUR PATTERN HERE", text)
print(f"All words: {all_words}")
```

#### Part 3: Practicing Exact Counts

```python
print("\n=== PRACTICING EXACT COUNTS ===")

# Task 5: Find all 5-digit numbers (like the IDs)
# {n} qunatifier
five_digit_numbers = re.findall(r"# YOUR PATTERN HERE", text)
print(f"5-digit numbers: {five_digit_numbers}")  # Should find: ['12345', '67890']

# Task 6: Find all 3-digit numbers
#hint: {n} quantifier
three_digit_numbers = re.findall(r"# YOUR PATTERN HERE", text)
print(f"3-digit numbers: {three_digit_numbers}")  # Should find: ['123', '678', '555', '123']
```

### What You're Practicing
- **`\d`** - finding digits
- **`\w`** - finding word characters  
- **`+`** - one or more repetitions
- **`{n}`** - exact number of repetitions
- **`re.search()`** - finding first match
- **`re.findall()`** - finding all matches

---

## Assignment 2: Customer Data Cleanup

### Scenario
You're working for a company's customer service team. Customer feedback often contains personal information that needs to be removed before sharing with other departments, and the text formatting is messy. Use `re.sub()` to clean it up!



### The Dataset
```python
import re

# Raw customer feedback from online form
feedback = "Great service! You can reach me at 555-0123 or    email me at john@email.com.    Overall    rating: 5 stars."
```

### Your Tasks

```python
print("=== CUSTOMER FEEDBACK CLEANUP ===")
print(f"Original feedback: {feedback}")

# Task 1: Remove phone numbers for privacy
# TODO: Replace phone numbers (like 555-0123) with "[PHONE REMOVED]"
no_phone = re.sub(r"# YOUR PATTERN HERE", "[PHONE REMOVED]", feedback)
print(f"Phone removed: {no_phone}")

# Task 2: Clean up extra spaces (common in web forms)
# TODO: Replace multiple spaces with single spaces using \s+
clean_spaces = re.sub(r"# YOUR PATTERN HERE", " ", no_phone)
print(f"Spaces fixed: {clean_spaces}")

print("\n=== CHECKING YOUR WORK ===")
print("The final text should:")
print("- Have no phone numbers")
print("- Have normal spacing")
```

### What You're Practicing
- **Privacy protection**: Removing sensitive information like phone numbers
- **Data cleaning**: Fixing formatting issues from web forms

### Expected Learning Outcomes
- Apply `re.sub()` to realistic data cleaning scenarios
- Understand why regex is useful for data privacy and cleanup
- See how regex solves real problems in customer service/data processing
- Feel confident handling messy user input data

---

## Bonus: Text Pattern Practice

### Scenario
Now that you understand basic grouping, practice extracting information from simple text patterns. This is a gentle introduction to using groups with real-world data.



### The Dataset
```python
import re

# Simple product data from an online store
product_data = """
Item: T-Shirt, Price: $25.99, Size: Large
Item: Jeans, Price: $45.50, Size: Medium  
Item: Sneakers, Price: $89.00, Size: 10
Item: Hat, Price: $15.75, Size: Small
"""
```

### Your Tasks

```python
print("=== PRODUCT INFORMATION EXTRACTION ===")

# Task 1: Extract just the product names using groups
print("Task 1: Product Names")
# TODO: Use groups to extract just the product name (between "Item: " and ",")
# Pattern hint: Item: (PRODUCT_NAME), Price:
for line in product_data.strip().split('\n'):
    match = re.search(r"Item: (\w+),", line)
    if match:
        product_name = match.group(1)
        print(f"Product: {product_name}")

print("\nTask 2: Extract Prices") 
# TODO: Use groups to extract just the price (after "$" and before ",")
# Pattern hint: \$(\d+\.\d+)
for line in product_data.strip().split('\n'):
    match = re.search(r"# YOUR PATTERN HERE", line)
    if match:
        price = match.group(1)
        print(f"Price: ${price}")

print("\nTask 3: Reformat Product Display")
# TODO: Use groups to extract name AND price, then reformat the output
# Show as: "PRODUCT_NAME costs $PRICE"
for line in product_data.strip().split('\n'):
    match = re.search(r"# YOUR PATTERN HERE", line)
    if match:
        name = match.group(1)
        price = match.group(2)
        print(f"{name} costs ${price}")
```

### What You're Practicing
- **`(pattern)`**: Creating groups to capture parts of matches
- **`.group(1), .group(2)`**: Accessing captured groups by number  
- **Real-world data**: Extracting information from structured text

### Expected Learning Outcomes
- Understand how to use groups to extract specific parts of text patterns
- Apply grouping to simple data processing tasks
- Build confidence with basic regex groups before moving to advanced patterns




### Expected Learning Outcomes
- Master named groups syntax: `(?P<name>pattern)`
- Extract structured data from unstructured text
- Apply regex groups to real-world log analysis
- Understand practical cybersecurity applications

---



## Quick Reference

### Common Regex Metacharacters
- `\d` - Any digit (0-9)
- `\w` - Word character (letters, digits, underscore)
- `\s` - Whitespace (space, tab, newline)
- `.` - Any character except newline
- `^` - Start of string
- `$` - End of string

### Quantifiers
- `+` - One or more
- `*` - Zero or more  
- `?` - Zero or one
- `{n}` - Exactly n times
- `{n,m}` - Between n and m times

### Groups
- `(pattern)` - Capturing group
- `(?P<n>pattern)` - Named group
- `(?:pattern)` - Non-capturing group

### Python re Functions
- `re.search(pattern, text)` - Find first match
- `re.findall(pattern, text)` - Find all matches
- `re.match(pattern, text)` - Match at start only
- `re.sub(pattern, replacement, text)` - Replace matches

Good luck with your regex practice! 