from flask import Flask, render_template
from dice import roll_die

app = Flask(__name__)


@app.route("/")
@app.route("/dice_game")
def dice_game():
    return render_template('dice.html', result=roll_die())


if __name__ == '__main__':
    app.run(debug=True)
