from app import db


class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    phone = db.Column(db.String(20))
    articles = db.relationship("Article")
