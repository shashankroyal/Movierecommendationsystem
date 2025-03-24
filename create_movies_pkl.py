import pickle
import pandas as pd

# Load the movie dictionary from the existing .pkl file
try:
    with open("movie_dict.pkl", "rb") as f:
        movie_dict = pickle.load(f)

    # Convert to DataFrame and save as movies.pkl
    df = pd.DataFrame(movie_dict)
    with open("movies.pkl", "wb") as f:
        pickle.dump(df, f)

    print("✅ movies.pkl has been created successfully!")

except FileNotFoundError:
    print("❌ Error: movie_dict.pkl file not found!")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")

