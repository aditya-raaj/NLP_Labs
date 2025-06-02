# ----------------------------------------
# Lab Program (b): Text Cleaning + Tokenization (Word, Subword, Character)
# Tokenization	word_tokenize(), sent_tokenize()
#Stopword Removal	stopwords.words('english')
# ----------------------------------------

import string
import nltk
import time
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# Download stopwords from NLTK corpus (only once)
nltk.download('stopwords')

# Define the main text processing function
def clean_text(file_path, output_file):
    try:
        # Step 1: Read the file content
        with open(file_path, 'r') as file:
            text = file.read()

        print("\n📄 Step 1: Original Text:\n")
        print(text)
        time.sleep(2)

        # Step 2: Convert to lowercase
        text = text.lower()
        print("\n🔻 Step 2: Lowercase Text:\n")
        print(text)
        time.sleep(2)

        # Step 3: Remove punctuation
        text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
        print("\n✂️ Step 3: Text without Punctuation:\n")
        print(text_no_punct)
        time.sleep(2)

        # -----------------------------
        # Step4 : Tokenization 
        # Word-Level Tokenization
        # -----------------------------
        # Splits the text into individual words using spaces
        word_tokens = text_no_punct.split()
        print("\n🟢 Step 4: Word Tokenization (Using .split()):\n")
        print(word_tokens)
        time.sleep(2)

        # -----------------------------
        # 🔤 Character-Level Tokenization
        # -----------------------------
        # Converts the text into a list of characters (excluding spaces)
        char_tokens = list(text_no_punct.replace(" ", ""))
        print("\n🔤 Step 5: Character Tokenization:\n")
        print(char_tokens)
        time.sleep(2)

        # -----------------------------
        # 🧩 Subword-Level Tokenization
        # -----------------------------
        # Breaks words into smaller chunks of 2–4 characters using Regex
        subword_tokenizer = RegexpTokenizer(r'\w{2,4}')
        subword_tokens = subword_tokenizer.tokenize(text_no_punct)
        print("\n🧩 Step 6: Subword Tokenization (Using RegexTokenizer):\n")
        print(subword_tokens)
        time.sleep(2)

        # -----------------------------
        # ❌ Stopword Removal : A stopword is a commonly occurring word in a language 
        # that does not carry significant meaning and is usually removed during NLP preprocessing.
        # -----------------------------
        stop_words = set(stopwords.words('english'))
        cleaned_word_tokens = [word for word in word_tokens if word not in stop_words]
        print("\n✅ Step 7: Word Tokens after Stopword Removal:\n")
        print(cleaned_word_tokens)
        time.sleep(2)

        # Save everything to output file
        with open(output_file, 'w') as out:
            out.write("Cleaned Word Tokens (Stopwords Removed):\n")
            out.write(' '.join(cleaned_word_tokens) + "\n\n")

            out.write("Character Tokens:\n")
            out.write(' '.join(char_tokens) + "\n\n")

            out.write("Subword Tokens (2–4 chars):\n")
            out.write(' '.join(subword_tokens))

        print(f"\n📁 Output saved to: {output_file}")

    except FileNotFoundError:
        print("❌ File not found. Please check the path.")

# ----------------------------------
# Run the function with your files
file_path = "C:/Users/Sowmya/Documents/NLP/NLP_Labs/Sample_input_labprg2.txt"
output_file = "C:/Users/Sowmya/Documents/NLP/NLP_Labs/Cleaned_output_all_tokens.txt"
clean_text(file_path, output_file)
