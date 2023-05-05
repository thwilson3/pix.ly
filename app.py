import boto3
import os
import PIL.Image

from flask import Flask, request
from flask_debugtoolbar import DebugToolbarExtension
from uuid import uuid4
from flask_cors import CORS


from models import db, connect_db, Picture
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']
S3_INFO = {
    "bucket": os.environ['BUCKET'],
    "region": "us-west-1"
}

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///pixly') #must link to db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True #always true to see sql in terminal

connect_db(app)


app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

s3 = boto3.client(
"s3",
"us-west-1",
aws_access_key_id=ACCESS_KEY,
aws_secret_access_key=SECRET_ACCESS_KEY,
)

@app.post('/api/add')
def add_picture():
    """Add picture to aws server/db and return html link"""
    file = request.files['image']

    open_file = PIL.Image.open(file)

    exif_data2 = open_file._getexif()

    print("file====================", exif_data2)

    file.seek(0)
    s3.upload_fileobj(file, S3_INFO['bucket'], file.filename)

    # #TODO: potentially try/except this line
    url = f"https://s3.{S3_INFO['region']}.amazonaws.com/{S3_INFO['bucket']}/{file.filename}"

    return url


#TODO: implement search below
@app.get('/api/pictures')
def search():
    """Either gets all pictures or searches for specific images """
    #if there is a query term in request then

    search = request.args.get('q')

    results = Picture.query.filter(Picture.description.match(search)).all()
    if not search:
        pictures = Picture.query.all()
    else:
        users = Picture.query.filter(Picture.username.like(f"%{search}%")).all()
