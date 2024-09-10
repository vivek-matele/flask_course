from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return f"<h1>Welcome to the home page</h1>"

@app.route("/pass/<s_name>/<int:marks>")
def passed():
    return f"<h1>Congratulations! {s_name.title()} You have passed with {marks} marks !</h1>"

@app.route("/failed/<s_name>/<int:marks>")
def failed():
    return f"<h1>Sorry {s_name.title()} You have failed fail with {marks} marks!</h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        # Redirect to fail webpage
        return redirect(url_for("failed",s_name=name,marks=num))
    else:
        return redirect(url_for("passed",s_name=name,marks=num))

if __name__ == "__main__":
    app.run(debug=True)