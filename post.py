import datetime
from application import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    titre = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(80), nullable=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
