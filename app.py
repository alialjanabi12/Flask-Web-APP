from flask import Flask, render_template

# -----------------
# created an app instance
# -----------------
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# -----------------
# execute the app
# -----------------
app.run(debug=True, port=5001)
