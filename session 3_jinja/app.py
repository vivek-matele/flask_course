from flask import Flask

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
@app.route('/home')
def home():
    return '<h1>Welcome to the home page!</h1>'


@app.route('/about')
def about():
    return "<h1> welcome to about page </h1>"


if __name__ == '__main__':
    app.run(debug=True)