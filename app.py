from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    print("I am in test_feature - Starting Flask app...")
    app.run(debug=True)
