from app import app #This needs to be here even if it isn't accessed
from models import db, Picture

# with app.app_context():

db.drop_all()
db.create_all()


picture1 = Picture(
    id=1,
    filename='picture1.jpg',
    location='New York City',
    orientation='Portrait',
)

picture2 = Picture(
    id=2,
    filename='picture2.jpg',
    location='San Francisco',
    orientation='Landscape',
)

picture3 = Picture(
    id=3,
    filename='picture3.jpg',
    location='France',
    orientation='Landscape',
)

picture4 = Picture(
    id=4,
    filename='picture3.jpg',
    location='Paris',
    orientation='Portrait',
)

picture5 = Picture(
    id=5,
    filename='800x600',
    location='Tokyo',
    orientation='Portrait',
)

db.session.add_all([picture1, picture2, picture3, picture4, picture5])
db.session.commit()
