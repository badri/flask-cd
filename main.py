from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app. Edited at 8:48 PM, 14th July 2024."})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
