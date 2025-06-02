# ----------------------------------------
# Program to extract email IDs from a Word file (.docx)
# ----------------------------------------

import re                            # To use regular expressions (Regex)
from docx import Document            # To read .docx Word files

# Function to extract emails from a given Word (.docx) file
def extract_emails_from_docx(file_path):
    try:
        # Step 1: Load the Word document
        doc = Document(file_path)

        # Step 2: Extract all text from paragraphs
        full_text = ""
        for para in doc.paragraphs:
            full_text += para.text + "\n"

        print("📄 Content read from file:\n")
        print(full_text)

        # Step 3: Define regex pattern for email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        # Step 4: Find all email matches in the text
        emails = re.findall(email_pattern, full_text)
        # Regular Expression Pattern to Match Email IDs:
# -----------------------------------------------
# [a-zA-Z0-9._%+-]+    → Matches the username part of the email.
#                        - Includes lowercase (a-z), uppercase (A-Z), digits (0-9)
#                        - And allowed special characters: dot (.), underscore (_), percent (%), plus (+), hyphen (-)
#                        - + means "one or more characters"

# @                    → The mandatory "@" symbol that separates username and domain

# [a-zA-Z0-9.-]+       → Matches the domain name (like gmail, yahoo, university)
#                        - Allows letters, digits, dots, and hyphens

# \.                   → Escaped dot (.) before domain extension (like .com, .in)
#                        - \. ensures we match a literal dot (not "any character")

# [a-zA-Z]{2,}         → Matches domain extension (like com, in, org, ac, edu)
#                        - Only letters allowed
#                        - {2,} means "at least 2 characters" (to ensure validity)

        # Step 5: Display the results
        print("\n📧 Extracted Email IDs:")
        if emails:
            for email in emails:
                print("→", email)
            print(f"\nTotal emails found: {len(emails)}")
        else:
            print("No email IDs found in the document.")

    except Exception as e:
        print("Error reading file:", e)

# -------------------------------
# Main execution with sample input
# -------------------------------

# Provide the file path of your Word document here
file_path = "./lab1_input.docx"
extract_emails_from_docx(file_path)
