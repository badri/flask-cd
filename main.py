from flask import Flask, jsonify
import os
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def index():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    app.logger.info(f'Request received at {timestamp}')
    return jsonify({"Choo Choo": "Welcome to your Flask app. Edited at 9:46 PM, 2nd August 2024."})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
