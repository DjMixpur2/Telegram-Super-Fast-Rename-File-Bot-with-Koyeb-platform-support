from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!", 200

@app.route("/health", methods=["GET"])
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
  
