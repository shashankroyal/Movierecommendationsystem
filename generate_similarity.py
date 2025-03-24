import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie dataset
try:
    df = pd.read_csv("movies.csv")  # Ensure this file exists
except FileNotFoundError:
    print("❌ Error: movies.csv file not found!")
    exit()

# Ensure 'tags' column exists (instead of 'description')
if 'tags' not in df.columns:
    print("❌ Error: 'tags' column missing from the dataset!")
    exit()

# Convert text descriptions (tags) into TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['tags'])

# Compute cosine similarity
similarity = cosine_similarity(tfidf_matrix)

# Save similarity matrix
with open("similarity.pkl", "wb") as f:
    pickle.dump(similarity, f)

print("✅ similarity.pkl has been created successfully!")
