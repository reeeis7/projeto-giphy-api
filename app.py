from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GIPHY_API_KEY = "1eOrPFudFMxU1wx3CSj1vjOAT1vHO8FB"
GIPHY_API_URL = "https://api.giphy.com/v1/gifs/search"

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    query = request.args.get("query")
    url = f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={query}&limit=5"
    response = requests.get(url)
    data = response.json()
    gifs = data.get("data", [])
    return render_template("index.html", gifs=gifs)


if __name__ == "__main__":
    app.run(debug=True)