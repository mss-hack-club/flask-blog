from flask.templating import render_template
from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")


@app.route('/login')
def login():
    return render_template('login.html', title="Login")


@app.route('/register')
def register():
    return render_template('register.html', title="Login")
