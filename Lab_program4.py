import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Sample text data
documents = [
    "Natural Language Processing is fun.",
    "Language models are part of NLP.",
    "We learn feature extraction in NLP lab."
]

# --- One-Hot Encoding ---
print("\n--- One-Hot Encoding ---")
df = pd.DataFrame({'Text': documents})
encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(df[['Text']])
print("Feature Names:", encoder.get_feature_names_out())
print(pd.DataFrame(encoded, columns=encoder.get_feature_names_out()))

# --- Count Vectorizer ---
print("\n--- Count Vectorizer ---")
cv = CountVectorizer()
cv_matrix = cv.fit_transform(documents)
print("Feature Names:", cv.get_feature_names_out())
print(pd.DataFrame(cv_matrix.toarray(), columns=cv.get_feature_names_out()))

# --- TF-IDF Vectorizer ---
print("\n--- TF-IDF Vectorizer ---")
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(documents)
print("Feature Names:", tfidf.get_feature_names_out())
print(pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out()))
