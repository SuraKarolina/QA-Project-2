from application import app
from application import db
from application.models import Match





if __name__ == "__main__":
    app.run(port=5000, debug=True)