import os

class Config:
    # Render will provide these. Locally, they will be None, flask will search in the instance forlder.
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
