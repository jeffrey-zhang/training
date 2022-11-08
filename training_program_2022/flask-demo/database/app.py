from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import os

app = Flask(__name__)

app.config.from_prefixed_env()

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "sqlite:///" + os.path.join(app.root_path, "database.db")
)

db = SQLAlchemy(app)
# import the db models
from models import note, author, article

migrate = Migrate(app, db)
