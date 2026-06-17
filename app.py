from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Use /<number> in the URL. Example: /10"

@app.route("/<int:number>")
def check(number):
    if number % 2 == 0:
        return f"{number} is Even"
    return f"{number} is Odd"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
