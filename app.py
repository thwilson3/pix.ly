import boto3
import os

from boto3 import ImportError
from flask import Flask, request, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from uuid import uuid4


from models import db, connect_db
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

bucket = os.environ['BUCKET']

@app.post('/api/add')
def add_picture():
    """Add picture to aws server/db and return html link"""
    filename = request.data
    obj_name = uuid4()

    #TODO: potentially try/except this line
    s3.upload_file(filename, bucket, obj_name)
    url = f"https://{S3_INFO['bucket']}.s3.{S3_INFO['region']}.amazonaws.com/{filename}"

    return url




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