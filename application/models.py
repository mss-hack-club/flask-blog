from application import db
from datetime import datetime
from flask_login import UserMixin


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Post('{self.title}, {self.date_posted})"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(60), nullable=False)
    posts = db.Relationship('Post', backref='author', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}, {self.email})"
