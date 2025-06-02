import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Sample text
text = "Natural Language Processing is a core subject in AI and ML."

# Tokenize
tokens = word_tokenize(text.lower())

# Generate N-grams
def generate_ngrams(tokens, n):
    return list(ngrams(tokens, n))

# Display results
print("\n--- Unigrams ---")
print(generate_ngrams(tokens, 1))

print("\n--- Bigrams ---")
print(generate_ngrams(tokens, 2))

print("\n--- Trigrams ---")
print(generate_ngrams(tokens, 3))
