"""
Lab Program 2: Text Standardization and Spell Correction
Updated to support any number of words, including names, acronyms, or typos.
Course: BAI601 - NLP (VI Semester, AI&ML)
Author: Sowmya
"""

import re
import nltk
import contractions
from spellchecker import SpellChecker

# Download tokenizer data
nltk.download('punkt', quiet=True)

# ----------------------------
# TEXT STANDARDIZATION
# ----------------------------
def standardize_text(text):
    """
    Standardizes input text:
    - Expands contractions
    - Removes non-alphabet characters
    - Converts to lowercase
    - Normalizes spacing
    """
    text = contractions.fix(text)
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)       # Keep only letters and space
    text = re.sub(r'\s+', ' ', text).strip()   # Normalize spaces
    return text

# ----------------------------
# SPELL CORRECTION
# ----------------------------
def correct_spelling(text):
    """
    Corrects spelling word-by-word using:
    - Custom correction dictionary (for known cases)
    - SpellChecker for others
    - Fallback to original word if no correction found
    """
    spell = SpellChecker()
    words = nltk.word_tokenize(text)

    # Custom corrections: for common or context-specific typos
    custom_corrections = {
        "ma": "am",
        "teh": "the",
        "langauge": "language",
        "dont": "don't",
        "isnt": "isn't",
        "wrng": "wrong"
    }

    corrected_words = []

    for word in words:
        if word in custom_corrections:
            corrected_words.append(custom_corrections[word])
        else:
            correction = spell.correction(word)
            if correction is None:
                corrected_words.append(word)  # Leave as-is
            else:
                corrected_words.append(correction)

    return ' '.join(corrected_words)

# ----------------------------
# MAIN PROGRAM
# ----------------------------
if __name__ == "__main__":
    print("\n NLP Lab Program 2: Spell Correction for Any Input\n")

    # Take flexible input
    user_input = input("🔸 Enter one or more words (with or without spelling errors):\n> ")

    # Step 1: Clean text
    standardized = standardize_text(user_input)
    print("\n🔹 Standardized Text:\n", standardized)

    # Step 2: Correct spelling
    corrected = correct_spelling(standardized)
    print("\n Corrected Output:\n", corrected)
