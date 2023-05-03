import boto3
import os

from flask import Flask, request, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from uuid import uuid4


from models import db, connect_db
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']


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

@app.post('/api/host')
def host_picture_on_server():
    """Host picture on aws server and return JSON of db record"""
    data = request.data




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