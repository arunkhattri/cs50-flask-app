import os
from flask import session, render_template, flash, redirect, url_for, request
from flask_session import Session
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm, SearchForm
from app import app, db
from app.models import User, Books
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgresql://postgres:8@ttle#1eld5@localhost:5432/cs50")
pg = scoped_session(sessionmaker(bind=engine))


@app.route("/")
@login_required
def index():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)


@app.route('/search', methods=['GET', 'POST'])
def search():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template("search.html", form=search)


@app.route('/results')
def search_results(search):
    """List all Books"""
    search_string = search.data['search']
    select_choice = search.data['select']
    if select_choice == 'isbn':
        results = pg.execute("SELECT * FROM books WHERE isbn = :isbn",
                             {"isbn": search_string}).fetchone()
        if results is None:
            return render_template("error.html",
                                   message="No such ISBN in the database.")
    elif select_choice == 'title':
        results = pg.execute("SELECT * FROM books WHERE title = :title",
                             {"title": search_string}).fetchone()
        if results is None:
            return render_template("error.html",
                                   message="No such Title in the database.")
    else:
        results = pg.execute("SELECT * FROM books WHERE author = :author",
                             {"author": search_string}).fetchone()
        if results is None:
            return render_template("error.html",
                                   message="No such Author in the database.")
    return render_template('results.html', results=results)


# TODO: results.html
# TODO: error.html
