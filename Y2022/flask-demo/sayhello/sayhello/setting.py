import os

from sayhello import app

dev_db = "sqlite:///" + os.path.join(os.path.dirname(app.root_path), "database.db")

SECRET_KEY = os.getenv("SECRET_KEY", "sayhello secret key")

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", dev_db)
