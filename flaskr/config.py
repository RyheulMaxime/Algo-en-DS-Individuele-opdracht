import os

class Config:
    # Render will provide these. Locally, they will be None (and that's okay for now).
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
