from app import app
from models import db, Pictures

with app.app_context():
    db.drop_all
    db.create_all()



picture1 = Pictures(
    id=1,
    dimension='1200x800',
    location='New York City',
    device_make='Canon',
    object_name='Statue of Liberty'
)

picture2 = Pictures(
    id=2,
    dimension='1600x900',
    location='San Francisco',
    device_make='Nikon',
    object_name='Golden Gate Bridge'
)

picture3 = Pictures(
    id=3,
    dimension='800x600',
    location='Paris',
    device_make='Sony',
    object_name='Eiffel Tower'
)

db.session.add_all([picture1, picture2, picture3])
db.session.commit()
