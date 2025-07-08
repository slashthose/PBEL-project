
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load the book data
with open("sample_books.json", "r") as f:
    books = json.load(f)

@app.route("/recommend", methods=["GET"])
def recommend():
    genre = request.args.get("genre", "").lower()
    author = request.args.get("author", "").lower()
    mood = request.args.get("mood", "").lower()

    results = books
    if genre:
        results = [book for book in results if genre in book["genre"].lower()]
    if author:
        results = [book for book in results if author in book["author"].lower()]
    if mood:
        results = [book for book in results if mood in book["mood"].lower()]

    if results:
        return jsonify(results[0])
    else:
        return jsonify({"error": "No matching book found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
