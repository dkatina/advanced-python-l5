import re
# from character_sets import email

#Without groups
text = "Contact: Johnny Boy Doe <jdoe@email.com>"

# basic_search = email.search(text)
# print(basic_search.group())


#With groups - () allow us to set up multiple patterns within text
contact = re.search(r"Contact: ([A-z ]+) <(\w+@\w+\.\w{2,3})>", text)

print(contact.group(1))
print(contact.group(2))


#named groups
contact = re.search(r"Contact: (?P<name>[A-z ]+) <(?P<email>\w+@\w+\.\w{2,3})>", text)

print(contact.group('email'))


# ========================================== Sub Groups to re-organize them
#Rearrange date format

date = "Metting 07/22/2025"

# Capture month, day, year into groups, and then rearrange them using sub

new_format = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", date)
print("Old String", date)
print("Reformated", new_format)