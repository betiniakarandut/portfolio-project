from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return "Welcome abode Betini Akarandut"


if __name__ == "__main__":
    app.run(debug=True)