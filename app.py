from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    print("Hi - Starting Flask app...")
    app.run(debug=True)
