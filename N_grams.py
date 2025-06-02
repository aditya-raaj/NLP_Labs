# Importing necessary modules
from collections import Counter  # Used to count frequency of tokens and n-grams
from nltk.util import ngrams     # Function to generate n-grams from a list of tokens

# -----------------------------
# STEP 1: Define the Corpus
# -----------------------------
corpus = "I am happy because I am learning"

# -----------------------------
# STEP 2: Preprocess the Corpus
# -----------------------------
tokens = corpus.lower().split()  # Lowercase and split into tokens
print("\nTokens:", tokens)
size_corpus = len(tokens)
print("\nSize of corpus:", size_corpus)

# -----------------------------
# STEP 3: UNIGRAMS
# -----------------------------
unigram_counts = Counter(tokens)
print("\nUnigram Counts:")
for unigram, count in unigram_counts.items():
    print(f"{unigram} : {count}")

print("\nUnigram Probabilities:")
for unigram, count in unigram_counts.items():
    probability = count / size_corpus
    print(f"P({unigram}) = {count}/{size_corpus} = {round(probability, 4)}")

# -----------------------------
# STEP 4: BIGRAMS
# -----------------------------
bigrams = list(ngrams(tokens, 2))
bigram_counts = Counter(bigrams)
print("\nBigram Counts:")
for bigram, count in bigram_counts.items():
    print(f"{bigram} : {count}")

print("\nBigram Probabilities:")
for bigram, count in bigram_counts.items():
    previous_word = bigram[0]
    prob = count / unigram_counts[previous_word]
    print(f"P({bigram[1]} | {previous_word}) = {count}/{unigram_counts[previous_word]} = {round(prob, 4)}")

# -----------------------------
# STEP 5: TRIGRAMS
# -----------------------------
trigrams = list(ngrams(tokens, 3))
trigram_counts = Counter(trigrams)
print("\nTrigram Counts:")
for trigram, count in trigram_counts.items():
    print(f"{trigram} : {count}")

print("\nTrigram Probabilities:")
for trigram, count in trigram_counts.items():
    previous_bigram = (trigram[0], trigram[1])
    previous_bigram_count = bigram_counts[previous_bigram]
    prob = count / previous_bigram_count
    print(f"P({trigram[2]} | {trigram[0]} {trigram[1]}) = {count}/{previous_bigram_count} = {round(prob, 4)}")

# -----------------------------
# STEP 6: INTERPRETATION OF RESULTS
# -----------------------------
print("\n" + "="*70)
print("INTERPRETATION OF N-GRAM RESULTS".center(70))
print("="*70)

print("\n1. 🔹 Why do we use N-grams?")
print("   - N-grams help us model how words are likely to follow one another.")
print("   - Useful in predicting next words, building translators, chatbots, and spell checkers.")

print("\n2. 🔹 Unigram Interpretation:")
print("   - Shows how frequently each word appears.")
print("   - E.g., 'i' and 'am' appear most (2/7 ≈ 28.57%), so they are most frequent.")

print("\n3. 🔹 Bigram Interpretation:")
print("   - Shows the probability of one word following another.")
print("   - P(am | i) = 1.0 → 'am' always follows 'i' in this sentence.")
print("   - P(happy | am) = 0.5 → 50% of the time 'happy' follows 'am'.")

print("\n4. 🔹 Trigram Interpretation:")
print("   - Takes 2-word history to predict the third word.")
print("   - P(happy | i am) = 0.5 → 'happy' follows 'i am' in 50% of cases.")
print("   - This richer context gives better accuracy for NLP tasks.")

print("\n5. 🔹 Practical Applications of N-grams:")
print("    Text Prediction (e.g., mobile keyboards)")
print("    Spell Correction (e.g., 'i hav' → 'i have')")
print("    Auto-suggestions in search engines")
print("    Machine Translation (e.g., Google Translate)")
print("   Speech Recognition and Chatbots")

print("\n6. 🔹 Limitations:")
print("    Cannot predict unseen sequences → leads to zero probability.")
print("    Cannot capture long-distance grammar dependencies.")
print("   Can be improved using Smoothing or Neural Language Models.")

print("\n7. Final Note:")
print("   - N-gram models are simple yet powerful tools for understanding and predicting language.")
print("   - Great for small to mid-sized applications and serve as the foundation for deeper NLP models.")
print("="*70 + "\n")
