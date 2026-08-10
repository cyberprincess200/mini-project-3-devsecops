from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "PayliteNG DevSecOps Demo"


@app.route("/search")
def search():
    query = request.args.get("q", "")
    return f"Search results for: {query}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
