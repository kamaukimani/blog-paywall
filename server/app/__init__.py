from flask import Flask 
from .db import db,migrate 
from .config import Config 
from .models import *
from .routes import *

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(article_bp,url_prefix='/articles')

    return app