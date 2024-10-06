import os
import uuid

# General Flask Config
SECRET_KEY = os.getenv("SECRET_KEY", str(uuid.uuid4()))
DEBUG = os.getenv("FLASK_DEBUG", False)

# Database Configuration
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///comet.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
