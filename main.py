from flask import Flask, jsonify
import os
from datetime import datetime
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route('/')
def index():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f'Request received at {timestamp}')
    return jsonify({"Choo Choo": "Welcome to your Flask app. Edited at 6:18 PM, 13th Oct 2024."})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
