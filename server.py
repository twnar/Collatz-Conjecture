from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

from collatz_core import TooManyStepsError, weird_algorithm

ROOT = Path(__file__).resolve().parent
app = Flask(__name__)


@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return response


@app.route("/")
def index():
    return send_from_directory(ROOT, "collatz.html")


@app.route("/compute", methods=["OPTIONS"])
def compute_options():
    return "", 204


@app.post("/compute")
def compute():
    data = request.get_json(silent=True) or {}
    raw = str(data.get("n", "")).replace(",", "").strip()

    if not raw or not raw.isdigit():
        return jsonify({"error": "Must be a positive whole number."}), 400

    if len(raw) > 10_000:
        return jsonify({"error": "Number too large — max 10,000 digits."}), 400

    n = int(raw)
    if n < 1:
        return jsonify({"error": "Must be a positive whole number."}), 400

    try:
        result = weird_algorithm(n)
    except TooManyStepsError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify(
        {
            "a": str(result["a"]),
            "steps": result["step"],
            "peak": str(result["peak"]),
            "sequence": [str(v) for v in result["full_sequence"]],
            "isCollatz": result["is_collatz"],
        }
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
