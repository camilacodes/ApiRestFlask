from flask import Flask


app = Flask(__name__)


if __name__ == "__main__":
    app.run(port=5001, debug=True)