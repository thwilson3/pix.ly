import boto3
import os

from flask import Flask, request, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from uuid import uuid4


from models import db, connect_db, Pictures
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']
S3_INFO = {
    "bucket": os.environ['BUCKET'],
    "region": "us-west-1"
}


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///pixly') #must link to db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True #always true to see sql in terminal

connect_db(app)

# upload_file(file_name, bucket, object_name)

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
    filename = request.data
    obj_name = uuid4()
    print('file - ADD ROUTE', request.files)
    # file = request.files['file']

    #TODO: potentially try/except this line
    s3.upload_file(filename, S3_INFO['bucket'] , obj_name)
    url = f"https://{S3_INFO['bucket']}.s3.{S3_INFO['region']}.amazonaws.com/{filename}"

    return url


@app.get('/api/pictures')
def search():
    """Either gets all pictures or searches for specific images """
    #if there is a query term in request then

    search = request.args.get('q')

    results = Pictures.query.filter(Pictures.description.match(search)).all()

    # if not search:
    #     pictures = Pictures.query.all()
    # else:
    #     users = Pictures.query.filter(User.username.like(f"%{search}%")).all()


# onSubmit:
#     filename = input.filename
#     obj_name = uuid4()
#     Pictures.add(...metadata, obj_name)
#     s3.upload_file(filename, bucketname, obj_name)

# onSearch:
#     term = input.term
#     picture_record = Pictures.query.all(where id = id)
#     html_link = s3.PresignedUrl(picture_record.obj_name, exp=3600)
#     return html_link