from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, world!!!</h1>'


@app.route('/about')
def about_page():
    return '<h1>About Page</h1>'


@app.route('/about/<username>')
def about_profile(username):
    return f'<h1>This is About Page of {username}</h1>'
