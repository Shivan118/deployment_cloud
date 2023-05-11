from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "Welcome to Data Science world"

if __name__ == "__main__":
    app.run(debug = True, port = "8080")