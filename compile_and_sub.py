import re
#Compile allows us to store frequently used patterns so we don't have to keep rewriting them
#Also becomes more efficient for our code

some_text = "This is some text here are some nums: 12343"
other_text = "This is the other num: 90008, 9873456"

nums = re.findall(r"\d+", some_text)
nums2 = re.findall(r"\d+", other_text)
print(nums)
print(nums2)


number_pattern = re.compile(r"\d+") #More efficient for the programmer AND the program itself

nums = number_pattern.findall(some_text)
nums2 = number_pattern.findall(other_text)
print(nums)
print(nums2)

#================== .sub() - allows us to replace things that fit a pattern with something specific

#Syntax: re.sub(sub_out, sub_in, text)

message = "I love cats and cats love me"

# Replace all cats with dogs
true_message = re.sub(r"cat", "dog", message)
print(true_message)

# Replace first digit groups in a phone number with "***"
my_phone = "Call me at: 877-237-1200"
protected = re.sub(r"\d{3}-\d{3}", "***-***", my_phone)
print(protected)


too_many_spaces = "This    is some     weird                text!"
cleaned = re.sub(r"\s+", " ", too_many_spaces)
print(cleaned)