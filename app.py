from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load movie dataset
df = pd.read_csv("movies.csv")

# Load similarity matrix
with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Function to get recommendations
def recommend(movie_title):
    if movie_title not in df['title'].values:
        return {"error": "Movie not found in the dataset!"}

    # Get movie index
    movie_idx = df[df['title'] == movie_title].index[0]

    # Get similarity scores
    scores = list(enumerate(similarity[movie_idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    # Prepare response
    recommendations = [{"title": df.iloc[idx]["title"], "score": round(score, 2)} for idx, score in sorted_scores]
    return {"movie": movie_title, "recommendations": recommendations}

# Route for Home Page
@app.route("/")
def home():
    return render_template("index.html")  # Ensure you have index.html in 'templates' folder

# API Route for Recommendations
@app.route("/recommend", methods=["POST"])
def get_recommendations():
    data = request.json
    movie_title = data.get("title", "").strip()

    if not movie_title:
        return jsonify({"error": "No movie title provided!"}), 400

    result = recommend(movie_title)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
