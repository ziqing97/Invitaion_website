from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    # settings
    from . import config
    app = Flask(__name__)
    app.config.from_object(config)
    
    # init DB
    db.init_app(app)

    # register bluprint
    from . import api
    app.register_blueprint(api.api)

    from . import views_home
    app.register_blueprint(views_home.bp)

    return app
