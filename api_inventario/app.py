from flask import Flask


app = Flask(__name__)

    

if __name__ == "__main__":
    app.run(port=8002, debug=True)