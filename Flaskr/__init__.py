import os

from flask import Flask
from .config import Config

from .db import db
from flask_login import LoginManager


login_manager = LoginManager()

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # 2. Load the default configuration (The Env Vars from Step 1)
    app.config.from_object(Config)

    # 3. Try to load 'config_local.py' from the instance folder.
    #    silent=True means: "If this file is missing (like on Render), just ignore it."
    #    If the file exists (locally), it overwrites the variables from Step 2.
    app.config.from_pyfile('config.py', silent=True)

    # 4. Initialize the database
    db.init_app(app)

    # 5. Initialize the login manager
    login_manager.init_app(app)
    login_manager.login_view = "login"

    # 6. Register the blueprints
    from .routes import main
    app.register_blueprint(main)
    
    
    return app


