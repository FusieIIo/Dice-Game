from flask import Flask, render_template
from dice import dice

app = Flask(__name__)


@app.route("/my_route")
def my_route():
    return render_template('dice.html'), dice()


if __name__ == '__main__':
    app.run(debug=True)
