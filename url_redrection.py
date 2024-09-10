from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return f"<h1>Welcome to the home page</h1>"

@app.route("/pass")
def passed():
    return f"<h1>Congratulations! You passed.</h1>"

@app.route("/failed")
def failed():
    return f"<h1>Sorry You have failed.</h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        # Redirect to fail webpage
        return redirect(url_for("failed"))
    else:
        return redirect(url_for("passed"))

if __name__ == "__main__":
    app.run(debug=True)







    




