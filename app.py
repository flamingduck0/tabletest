from flask import Flask, render_template, jsonify

import pythonfunctions
import os

data = pythonfunctions.give_data()
fencers = pythonfunctions.fencers(data)

app = Flask(__name__)

@app.route('/')
def home_page():  # put application's code here
    output = render_template('home.html', data=data, fencers=fencers)
    return output

if __name__ == '__main__':
    app.run(app)
