"""SQLAlchemy models for Pixley"""

from flask_sqlalchemy import SQLAlchemy
from ts_vector import TSVector
import sqlalchemy as sa
from sqlalchemy import Index

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)



class Picture(db.Model):
    """Photos in the system. """

    __tablename__ = "pictures"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    filename = db.Column(
        db.Text,
    )

    location = db.Column(
        db.Text,
        nullable=True,
    )

    orientation = db.Column(
        db.Text,
    )


    __ts_vector__ = db.Column(TSVector(),db.Computed(
         "to_tsvector('english', filename || ' ' || location || ' ' || location || ' ' || orientation)",
         persisted=True))
    # __table_args__ = (Index('ix_pictures___ts_vector__',
    #       __ts_vector__, postgresql_using='gin'),)




# user uploads photo
# -> backend get their exif data from the photo
# -> store in db(some id === aws id)
# -> send pic to aws
# -> user searches for photo
# -> query the db
# -> retrieve from aws and serve it

