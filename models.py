"""SQLAlchemy models for Pixley"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pictures(db.Model):
    """Photos in the system. """

    __tablename__ = 'pictures'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    dimension = db.Column(
        db.Text,
    )

    location = db.Column(
        db.Text,
        nullable=True,
    )

    device_make = db.Column(
        db.Text,
    )

    object_name = db.Column(
        db.Text,
    )


# user uploads photo
# -> backend get their exif data from the photo
# -> store in db(some id === aws id)
# -> send pic to aws
# -> user searches for photo
# -> query the db
# -> retrieve from aws and serve it

