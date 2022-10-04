from reader import read_file
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    val = read_file("./example.csv")
    return val