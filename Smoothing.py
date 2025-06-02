from collections import Counter, defaultdict
from nltk.util import ngrams
import math

# -----------------------------
# STEP 1: Define and preprocess the corpus
# -----------------------------
# A small training corpus to simulate real-world learning
corpus = "I love NLP and I love Python"
tokens = corpus.lower().split()
vocab = set(tokens)
V = len(vocab)  # Vocabulary size

# -----------------------------
# STEP 2: Count unigrams and bigrams
# -----------------------------
unigram_counts = Counter(tokens)
bigram_counts = Counter(ngrams(tokens, 2))

# -----------------------------
# STEP 3: Function to generate next word candidates
# -----------------------------
def next_word_prediction(prev_word, smoothing='laplace', k=0.5):
    candidates = list(vocab.union({'cats', 'dogs', 'music'}))  # Some valid unseen words
    probabilities = {}

    for word in candidates:
        bigram = (prev_word, word)
        count_bigram = bigram_counts[bigram]
        count_prev = unigram_counts[prev_word]

        if smoothing == 'none':
            # Raw probability (can be zero)
            prob = count_bigram / count_prev if count_prev > 0 else 0

        elif smoothing == 'laplace':
            # Add-1 (Laplace) Smoothing
            prob = (count_bigram + 1) / (count_prev + V)

        elif smoothing == 'add-k':
            # Add-k Smoothing
            prob = (count_bigram + k) / (count_prev + k * V)

        else:
            prob = 0  # fallback

        probabilities[word] = round(prob, 4)

    # Sort suggestions by highest probability
    sorted_probs = dict(sorted(probabilities.items(), key=lambda x: x[1], reverse=True))

    return sorted_probs

# -----------------------------
# STEP 4: Run predictions for "love"
# -----------------------------
predictions_raw = next_word_prediction("love", smoothing='none')
predictions_laplace = next_word_prediction("love", smoothing='laplace')
predictions_addk = next_word_prediction("love", smoothing='add-k', k=0.5)

# Prepare display tables
import pandas as pd

df_final = pd.DataFrame({
    'Next Word': predictions_raw.keys(),
    'Raw P(word | "love")': predictions_raw.values(),
    'Laplace P(word | "love")': predictions_laplace.values(),
    'Add-k P(word | "love") (k=0.5)': predictions_addk.values()
})

# Show table
import ace_tools as tools; tools.display_dataframe_to_user(name="Next Word Prediction After Smoothing", dataframe=df_final) # type: ignore
