from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "ok", "version": os.getenv("APP_VERSION","1.0.0"),
                    "env": os.getenv("ENV","local") })

@app.route('/health')
def health():
    return jsonify({"healthy": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
