import re

# Raw customer feedback from online form
feedback = "Great service! You can reach me at 555-0123 or    email me at john@email.com.    Overall    rating: 5 stars."


print("=== CUSTOMER FEEDBACK CLEANUP ===")
print(f"Original feedback: {feedback}")

# Task 1: Remove phone numbers for privacy
# TODO: Replace phone numbers (like 555-0123) with "[PHONE REMOVED]"
no_phone = re.sub(r"\d{3}-\d{4}", "[PHONE REMOVED]", feedback)
print(f"Phone removed: {no_phone}")

# Task 2: Clean up extra spaces (common in web forms)
# TODO: Replace multiple spaces with single spaces using \s+
clean_spaces = re.sub(r"\s+", " ", no_phone)
print(f"Spaces fixed: {clean_spaces}")

print("\n=== CHECKING YOUR WORK ===")
print("The final text should:")
print("- Have no phone numbers")
print("- Have normal spacing")

email = re.search(r"\w+@\w+\.\w{2,3}", feedback)
print(email.group())