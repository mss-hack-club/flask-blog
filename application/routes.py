from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from application import app, db
from flask_login import login_user, current_user, logout_user, login_required
from application.forms import LoginForm, PostForm, RegistrationForm
from application.models import Post
from flask import flash, abort, request

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
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title="Create Post", form=form, legend="Create Post")


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title="Update Post")


@app.route('/post/<int:post_id>/update', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))
