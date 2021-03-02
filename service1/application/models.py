from application import db


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_sign = db.Column(db.String(100), nullable=False)
    second_sign = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(5000), nullable=False)