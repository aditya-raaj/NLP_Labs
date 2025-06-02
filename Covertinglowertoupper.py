import string

text = "Welcome to NLP Lab! We're learning how to clean, tokenize & process text."

# Convert to lowercase
text = text.lower()

# Remove punctuation
cleaned = "".join(char for char in text if char not in string.punctuation)

print("Cleaned Text:\n", cleaned)
