from reader import read_file
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    val = read_file("./example.csv")

    res = []
    for key, value in val.items():
        iter = int(value[0])
        for x in range (0, iter):
            res.append(key)
    return res