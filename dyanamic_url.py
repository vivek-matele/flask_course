from flask import Flask


app=Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return f"<h1> This is home page </h1>"
# dyanamic url
@app.route("/welcome/<name>")
def welcome_steve(name):
    return f"<h1>hi {name.title()} you r welcome on this page</h1>"

# @app.route("/welcome/vivek")
# def welcome_vivek():
#     return f"<h1>hi vivek you r welcome on this page</h1>"


if __name__ == "__main__":
    app.run(debug=True,port=5001)
