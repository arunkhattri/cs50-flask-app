import os

from flask import Flask, session, render_template
from flask_session import Session
# from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from forms import LoginForm

app = Flask(__name__)
# app.config.from_object(Config)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


# @app.route("/")
# def index():
#     return render_template("home.html")


# @app.route("/login")
# def login():
#     form = LoginForm()
#     return render_template("login.html", form=form)
