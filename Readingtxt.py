# Program : Extract Email IDs from a Text File using Regular Expressions

# Step 1: Import required libraries
import re   # 're' module provides support for regular expressions

# Step 2: Read contents from a text file
with open("C:/Users/Sowmya/Desktop/Sample.txt", "r") as file:  # Opens the file in read mode
    content = file.read()  # Reads the entire content of the file into a string

# Step 3: Define a regular expression pattern for email IDs
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  
# Explanation:
# [a-zA-Z0-9._%+-]+    => user name part (can have ., _, %, etc.)
# @                    => mandatory symbol

# [a-zA-Z0-9.-]+       => domain name
# \.[a-zA-Z]{2,}       => domain suffix like .com, .org, etc.

# Step 4: Use 'findall' to extract all matching emails from the text
emails_found = re.findall(email_pattern, content)

# Step 5: Display the results
print("\n📧 Email IDs Found:")
for email in emails_found:
    print(email)

print(f"\nTotal Emails Found: {len(emails_found)}")
