from flask import Flask

from flask import render_template

from flask import request

from dice import roll_die

app = Flask(__name__)


@app.route('/dice-game')

def dice_game():

    return render_template(

        'dice.html',

        result1=request.args.get('result1', type=int) or roll_die(),

        result2=roll_die())


if __name__ == '__main__':

    app.run(debug=True)
