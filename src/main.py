from flask import Flask
from flask import jsonify
from dotenv import dotenv_values
import asyncio


config = dotenv_values(".env")
app = Flask(__name__)

CLIENT_LIMIT = int(config['CLIENT_LIMIT']) if config['CLIENT_LIMIT'] else 3
sem = asyncio.Semaphore(CLIENT_LIMIT)


@app.route("/health_check")
def health_check():
    return ("OK", 200)
