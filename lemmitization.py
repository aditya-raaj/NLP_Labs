# Importing WordNetLemmatizer and pos_tag from nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag, download

# Download required nltk resources
download('wordnet')
download('averaged_perceptron_tagger')

# Function to map NLTK POS tags to WordNet tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # default to noun

# Creating lemmatizer object
lemmatizer = WordNetLemmatizer()

sentence = "The children were playing happily in the gardens."

# Tokenizing and POS tagging
words = sentence.split()
tagged_words = pos_tag(words)

# Applying lemmatization
for word, tag in tagged_words:
    lemma = lemmatizer.lemmatize(word, get_wordnet_pos(tag))
    print(f"{word} ({tag}) -> {lemma}")
