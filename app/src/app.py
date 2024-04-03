# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print('hi')
    print('hola hola hola')
    print('hello world')
    return "Hello world and everyone in it"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
