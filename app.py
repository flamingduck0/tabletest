from flask import Flask, render_template
from flask_socketio import SocketIO, send

import pythonfunctions
import os

data = pythonfunctions.give_data()
fencers = pythonfunctions.fencers(data)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["FLASK_SECRET"]
socketio = SocketIO(app)


@app.route('/')
def home_page():  # put application's code here
    output = render_template('home.html', data=data, fencers=fencers)
    return output

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

if __name__ == '__main__':
    app.run(app)
