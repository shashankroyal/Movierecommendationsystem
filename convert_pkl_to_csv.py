import pickle
import pandas as pd

# Load the movies.pkl file
try:
    with open("movies.pkl", "rb") as f:
        movies = pickle.load(f)

    # Convert it into a CSV file
    df = pd.DataFrame(movies)
    df.to_csv("movies.csv", index=False)
    
    print("✅ movies.csv has been created successfully!")

except FileNotFoundError:
    print("❌ Error: movies.pkl file not found!")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")
