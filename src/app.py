from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is a CICD demo using flask app"

if __name__ == "__main__":
    app.run()