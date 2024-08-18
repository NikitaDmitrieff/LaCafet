from flask import Flask

import views
from models import db


def create_app():

    from instances_generator import bcrypt, load_user, login_manager

    # create and configure the app
    app = Flask(__name__)

    app.config.from_pyfile("config.py", silent=True)

    db.init_app(app)
    bcrypt.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "Comet.login"
    login_manager.user_loader(load_user)

    app.register_blueprint(views.bp)

    with app.app_context():
        db.create_all()

    return app
