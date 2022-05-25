from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/table")
def tableau():
    return render_template("tableau.html")

if __name__ == "__main__":
    app.run(debug = True)
