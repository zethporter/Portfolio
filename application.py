from flask import Flask, render_template

application = app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")