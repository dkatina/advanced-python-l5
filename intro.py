import re #Importing the Regex package (Regular Expression)

#Re.search() - finds the FIRST match in the text, and return a match object

sample = "I love Python programming. Python is awesome for data science"

python = re.search(r"Python", sample)
# Syntacx: re.search(pattern, text_we_search)

print(python) #Prints a match object

#unpack match object with .group()
print(python.group()) #Shows the text we matched
print(python.start()) #Shows the start index
print(python.end()) #Shows the end index
print(python.span()) #Tuple with both the start and the end


java_match = re.search(r"Java", sample) #r string stands for raw (required for metacharacter patterns)

print(java_match) #Returns None if there is no match
#Always want to check if you have a match before calling group.
if java_match:
    print(java_match.group())
else:
    print("No Java")

def search_string(text):
    response = input("What would you like to search for?")
    my_match = re.search(f"{response}",text)
    try:
        print(f"Found {my_match.group()} starting at index {my_match.start()}")
    except:
        print("No Match found")

search_string(sample)

#1. search() - find the first instance of a pattern in text, returns a match object.

#2. findall() - Finds all occurances of a pattern, returns a list of strings

#3. match() - Check if text starts with specific pattern, returns match object

#4. sub() - Find and replace text (more powerful version of .replace())
