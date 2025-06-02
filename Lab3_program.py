import nltk
from docx import Document
import os
from nltk.tokenize import (
    sent_tokenize, word_tokenize, TreebankWordTokenizer,
    RegexpTokenizer, WordPunctTokenizer
)
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
from nltk import pos_tag

# === Load offline resources (assumes already downloaded once)
# Remove nltk.download(...) if running offline
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')

# === Input File Path (change accordingly)
input_file_path = "./NLP_Lab3_Input.docx"

# === Load File Content ===
def load_input_text(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == ".docx":
        doc = Document(file_path)
        return "\n".join(para.text for para in doc.paragraphs)
    else:
        raise ValueError("Unsupported file type. Use .txt or .docx only.")

text = load_input_text(input_file_path)

# === Initialize Tools ===
porter = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
treebank_tokenizer = TreebankWordTokenizer()
regex_tokenizer = RegexpTokenizer(r'\w+')
word_punct_tokenizer = WordPunctTokenizer()

# === Tokenization ===
sentence_tokens = sent_tokenize(text)
word_tokens_default = word_tokenize(text)
treebank_tokens = treebank_tokenizer.tokenize(text)
regex_tokens = regex_tokenizer.tokenize(text)
punct_tokens = word_punct_tokenizer.tokenize(text)
char_tokens = list(text.replace(" ", "").replace("\n", ""))

# === Subword Tokenization (manual)
subword_tokens = []
for word in regex_tokens:
    if len(word) > 6:
        mid = len(word) // 2
        subword_tokens.extend([word[:mid], word[mid:]])
    else:
        subword_tokens.append(word)

# === Stemming
stemmed_output = [(token, porter.stem(token)) for token in regex_tokens if token.isalpha()]

# === Lemmatization
lemmatized_output_simple = [(token, lemmatizer.lemmatize(token)) for token in regex_tokens if token.isalpha()]
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
pos_tags = pos_tag(regex_tokens)
lemmatized_output_advanced = [
    (word, lemmatizer.lemmatize(word, get_wordnet_pos(pos)))
    for word, pos in pos_tags if word.isalpha()
]

# === Stopword Removal
filtered_tokens = [token for token in regex_tokens if token.lower() not in stop_words and token.isalpha()]

# === DISPLAY OUTPUT ===

print("\n" + "="*80)
print("NLP Lab 3 – Tokenization, Stemming, and Lemmatization")
print("="*80)

# Sentence Tokenization
print("\n1. Sentence Tokenization (each line shows one sentence):")
for i, sent in enumerate(sentence_tokens, 1):
    print(f"{i}. {sent}")

# Word Tokenization
print("\n2. Word Tokenization Methods:")
print("Default Tokenizer:", word_tokens_default[:20], "...")
print("Treebank Tokenizer:", treebank_tokens[:20], "...")
print("Regex Tokenizer (words only):", regex_tokens[:20], "...")
print("WordPunct Tokenizer:", punct_tokens[:20], "...")

# Character Tokenization
print("\n3. Character-Level Tokenization:")
print("First 100 characters:", char_tokens[:100], "...")

# Subword Tokenization
print("\n4. Subword-Level Tokenization (manual split of long words):")
print(subword_tokens[:20], "...")

# Stemming
print("\n5. Stemming Output (Porter Stemmer):")
for word, stem in stemmed_output[:15]:
    print(f"{word} ➝ {stem}")

# Lemmatization (Basic)
print("\n6. Lemmatization Output (Basic - assumes noun):")
for word, lemma in lemmatized_output_simple[:15]:
    print(f"{word} ➝ {lemma}")

# Lemmatization (Advanced with POS)
print("\n7. Lemmatization Output (Advanced with POS tags):")
for word, lemma in lemmatized_output_advanced[:15]:
    print(f"{word} ➝ {lemma}")

# Stopword Removal
print("\n8. Tokens After Stopword Removal:")
print(filtered_tokens[:20], "...")

# Observations
print("\n9. Summary Observations:")
print("- Sentence tokenizer detects sentence boundaries.")
print("- Word-level tokenizers split using grammar or regex.")
print("- Character tokenization shows text at character level.")
print("- Subword split is manual: shows part-wise slicing.")
print("- Stemming is rule-based: cuts suffixes crudely.")
print("- Simple lemmatization returns dictionary form assuming noun.")
print("- Advanced lemmatization uses grammar context for better accuracy.")
