from flask_sqlalchemy import SQLAlchemy
from flask import (Flask, render_template, request,
                   Response, redirect, url_for, jsonify, abort)


database_name = "capstone"
database_path = "postgres://admeokiwakdldw:29015e30c1e200707aeca46f6a5fd212e75d7c112e1aa692568150533dbeca67@ec2-3-223-21-106.compute-1.amazonaws.com:5432/dc2h6aqcn1mdje"
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.Date)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
