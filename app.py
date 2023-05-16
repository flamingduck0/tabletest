from flask import Flask, render_template
from flask_socketio import SocketIO
import loadfile
import os

data = loadfile.give_data()
fencers = list(data['fencers'].keys())

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["FLASK_SECRET"]
socketio = SocketIO(app)


@app.route('/')
def home_page():  # put application's code here
    output = render_template('home.html', data=data, fencers=fencers)
    return output


if __name__ == '__main__':
    app.run(app)
