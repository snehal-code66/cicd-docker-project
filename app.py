from flask import Flask, jsonify
from datetime import datetime, timezone
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "CI/CD Pipeline with GitHub Actions & Docker",
        "status": "Running",
        "message": "Hello from DevOps Project!",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000))
    )
