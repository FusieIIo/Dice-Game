import random
from flask import render_template


def dice():
    return random.randint(1, 6), render_template('dice.html')


dice()
