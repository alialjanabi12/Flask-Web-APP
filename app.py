from flask import Flask, render_template, request

"""-----------------
 created an app instance
-----------------"""
app = Flask(__name__)

"""-----------------
create a route , this url will handle both get and post request
    - 'post' is when the user submits the form
    - 'get' is when the user navigates to the page
    - add <form method="post"> in the html under the form

-----------------"""


@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]

    return render_template("index.html")


"""-----------------
execute the app
-----------------"""
app.run(debug=True, port=5001)
