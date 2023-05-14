from flask import Flask, render_template
import loadfile

data = loadfile.give_data()

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    output = render_template('home.html', data=data)
    return output


if __name__ == '__main__':
    app.run()
