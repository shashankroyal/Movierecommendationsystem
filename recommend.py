import pandas as pd
import pickle

# Load movie dataset
df = pd.read_csv("movies.csv")  # Ensure this file exists

# Load the similarity matrix
with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Function to recommend movies
def recommend(movie_title):
    if movie_title not in df['title'].values:
        print("❌ Movie not found in the dataset!")
        return
    
    # Get the index of the movie
    movie_idx = df[df['title'] == movie_title].index[0]

    # Get similarity scores and sort movies based on similarity
    scores = list(enumerate(similarity[movie_idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]  # Top 5 recommendations

    # Display recommendations
    print(f"\n🎬 **Movies similar to {movie_title}:**")
    for i, (index, score) in enumerate(sorted_scores, start=1):
        print(f"{i}. {df.iloc[index]['title']} (Similarity: {score:.2f})")

# Run the recommendation system
if __name__ == "__main__":
    user_input = input("Enter a movie title: ")
    recommend(user_input)
