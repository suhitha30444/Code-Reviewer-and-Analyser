from flask import Flask, render_template, request, jsonify
from analyzer import analyze_code
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/review", methods=["POST"])
def review():
    data = request.get_json()
    code = data.get("code", "").strip()
    language = data.get("language", "python")
    if not code:
        return jsonify({"error": "No code provided"}), 400
    feedback = analyze_code(code, language)
    return jsonify({"feedback": feedback})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)