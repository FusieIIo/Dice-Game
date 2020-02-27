from flask import Flask
from dice import dice

app = Flask(__name__)


@app.route("/")
@app.route("/my_route")
def my_route():
    return dice()


if __name__ == '__main__':
    app.run(debug=True)
