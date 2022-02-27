"""
This is the main application file
"""
import os
import flask
from flask import Flask, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from tmdb_and_wiki import get_movie_data

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
uri = os.getenv("DATABASE_URL")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret-key-goes-here"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# class Reviews(db.Model):
# id = db.Column(db.Integer, primary_key=True)
# movieID = db.Column(db.Integer)
# comment = db.Column(db.String(128))
# rating = db.Column(db.Integer)


class UserReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    movieID = db.Column(db.Integer)
    comment = db.Column(db.String(128))
    rating = db.Column(db.Integer)


db.create_all()


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    # login code goes here
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(
            url_for("login")
        )  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for("index"))


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(
        email=email
    ).first()  # if this returns a user, then the email already exists in database

    if (
        user
    ):  # if a user is found, we want to redirect back to signup page so user can try again
        flash("Email address already exists")
        return redirect(url_for("signup"))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password, method="sha256"),
    )

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("login"))


@app.route("/profile")
@login_required
def profile():
    your_comments = UserReview.query.filter_by(email=current_user.email).all()
    num_comments = len(your_comments)
    return render_template(
        "profile.html",
        name=current_user.name,
        your_comments=your_comments,
        num_comments=num_comments,
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/", methods=["POST", "GET"])
@login_required
def index():
    """
    This functions retrieves movie data and sends it to the index.html file
    """
    movie_data = get_movie_data()
    reviews = UserReview.query.filter_by(movieID=movie_data["ids"][0]).all()
    num_reviews = len(reviews)

    return render_template(
        "index.html",
        titles=movie_data["titles"],
        poster_paths=movie_data["poster_paths"],
        taglines=movie_data["taglines"],
        ids=movie_data["ids"],
        genres=movie_data["genres"],
        wikilinks=movie_data["wikilinks"],
        reviews=reviews,
        num_reviews=num_reviews,
    )


@app.route("/review_added", methods=["GET", "POST"])
@login_required
def review_added():
    if flask.request.method == "POST":
        data = flask.request.form
        new_user_review = UserReview(
            name=current_user.name,
            email=current_user.email,
            movieID=request.form.get("movieID"),
            comment=request.form.get("comment"),
            rating=request.form.get("rating"),
        )
        if (
            UserReview.query.filter_by(
                email=current_user.email,
                movieID=new_user_review.movieID,
                comment=new_user_review.comment,
                rating=new_user_review.rating,
            ).first()
        ) is None:
            db.session.add(new_user_review)
            db.session.commit()
        else:
            return flask.redirect("/")

    movie_data = get_movie_data()
    reviews = UserReview.query.filter_by(movieID=movie_data["ids"][0]).all()
    num_reviews = len(reviews)
    return flask.render_template(
        "index.html",
        reviews=reviews,
        num_reviews=num_reviews,
        titles=movie_data["titles"],
        poster_paths=movie_data["poster_paths"],
        taglines=movie_data["taglines"],
        ids=movie_data["ids"],
        genres=movie_data["genres"],
        wikilinks=movie_data["wikilinks"],
    )


app.run(
    host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080")), debug=True
)
