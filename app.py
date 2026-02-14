# -----------------------------
# IMPORT REQUIRED MODULES
# -----------------------------
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


# -----------------------------
# CREATE FLASK APPLICATION
# -----------------------------
app = Flask(__name__)

# Configure application settings
app.config["SECRET_KEY"] = "mysecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Initialize database instance
db = SQLAlchemy(app)


# -----------------------------
# DEFINE DATABASE MODEL
# -----------------------------
class Form(db.Model):
    # Define table columns with data types
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    occupation = db.Column(db.String(80), nullable=False)


# -----------------------------
# DEFINE ROUTES
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handle both GET and POST requests.
    - GET: Display the form page.
    - POST: Process submitted form data.
    """
    print(request.method)

    if request.method == "POST":
        # Retrieve form data from HTML form
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]

    return render_template("index.html")


# -----------------------------
# RUN APPLICATION
# -----------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables if they do not exist
    app.run(debug=True, port=5001)
