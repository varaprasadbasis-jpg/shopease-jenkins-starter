import os
from flask import Flask, jsonify

app = Flask(__name__)

PRICES = {"laptop": 55000, "headphones": 2500, "keyboard": 1200}


@app.route("/")
def home():
    return jsonify(service="shopease-api",
                   version=os.getenv("APP_VERSION", "dev"),
                   environment=os.getenv("APP_ENV", "local"))


@app.route("/health")
def health():
    return jsonify(status="ok",
                   version=os.getenv("APP_VERSION", "dev"),
