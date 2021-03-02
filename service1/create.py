from application import db
from application.models import Match

db.drop_all()
db.create_all()

db_data = Match(first_sign = first_sign.text, second_sign = second_sign.text, description = description.text)
db.session.add(db_data)
db.session.commit()