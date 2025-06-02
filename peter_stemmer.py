# Importing the PorterStemmer from NLTK
from nltk.stem import PorterStemmer

# Creating the stemmer object
ps = PorterStemmer()

# List of example words
words = ["playing", "played", "plays", "player", "happiness", "happier", "running"]

# Applying stemming
for word in words:
    print(f"{word} -> {ps.stem(word)}")
