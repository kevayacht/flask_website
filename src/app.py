from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
CSRFProtect(app)


@app.route('/')
def home():
    return render_template('home.html',title='Home')


@app.route('/<string:page_name>/')
def landing_page(page_name):
    return render_template('%s.html' % page_name)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
