# Basic flask app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Cloud DevOps Engineer Capstone Project by Steven"

app.run(host="0.0.0.0", port=80)