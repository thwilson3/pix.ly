from app import app #This needs to be here even if it isn't accessed
from models import db, Pictures

# with app.app_context():

db.drop_all()
db.create_all()



picture1 = Pictures(
    id=1,
    dimension='1200x800',
    location='New York City',
    device_make='Canon',
    object_name='test1'
)

picture2 = Pictures(
    id=2,
    dimension='1600x900',
    location='San Francisco',
    device_make='Nikon',
    object_name='test2'
)

picture3 = Pictures(
    id=3,
    dimension='800x600',
    location='Paris',
    device_make='Sony',
    object_name='test3'
)

db.session.add_all([picture1, picture2, picture3])
db.session.commit()
