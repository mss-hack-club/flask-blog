from flask.templating import render_template
from application import app
from flask_login import login_user, current_user, logout_user, login_required
from application.forms import LoginForm, PostForm, RegistrationForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)

@app.route('/post/new')
def new_post():
    form = PostForm()
    return render_template('create_post.html', title="Create Post", form=form)
