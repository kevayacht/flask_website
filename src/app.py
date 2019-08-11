from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/<string:page_name>/')
def landing_page(page_name):
    return render_template('%s.html' % page_name)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
