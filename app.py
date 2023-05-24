from flask import Flask, render_template, jsonify

import pythonfunctions

tableList = pythonfunctions.table_as_list()
fencers = pythonfunctions.fencers()


app = Flask(__name__)

@app.route('/')
def home_page():  # put application's code here
    output = render_template('home.html', tableList=tableList, fencers=fencers)
    return output

if __name__ == '__main__':
    app.run(app)
