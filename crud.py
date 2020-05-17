from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, String

import copy
import json

from app.models.song import Song

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(user=SECRET["user"],
                                                                              password=SECRET["password"],
                                                                              host=SECRET["host"],
                                                                              port=SECRET["port"],
                                                                              db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Song_py(Song, db.Model):
    id = Column(Integer, primary_key=True)
    name = db.Column(String(50), unique=False)
    duration_in_min = Column(Integer, unique=False)
    year = Column(Integer, unique=False)
    singer = Column(String(50), unique=False)
    genre = Column(String(50), unique=False)
    album = Column(String(50), unique=False)

    def __init__(self, name="unknown", duration_in_min=0, singer="noname", year=2000, genre="uncknown", album="noname"):
        super().__init__(name, duration_in_min, singer, year)
        self.genre = genre
        self.album = album


class SongSchema(ma.Schema):
    class Meta:
        fields = ('name', 'duration_in_min', 'singer', 'year', 'genre', 'album')


song_schema = SongSchema()
songs_schema = SongSchema(many=True)


@app.route("/songpy", methods=["POST"])
def add_song_py():
    name = request.json['name']
    duration_in_min = request.json['duration_in_min']
    singer = request.json['singer']
    year = request.json['year']
    genre = request.json['genre']
    album = request.json['album']
    song_py = Song_py(name, duration_in_min, singer, year, genre, album)

    db.session.add(song_py)
    db.session.commit()
    return song_schema.jsonify(song_py)


@app.route("/songpy", methods=["GET"])
def get_songs_py():
    all_song_py = Song_py.query.all()
    result = songs_schema.dump(all_song_py)
    return jsonify({'song_py': result})


@app.route("/songpy/<id>", methods=["GET"])
def get_song_py(id):
    song_py = Song_py.query.get(id)
    if not song_py:
        abort(404)
    return song_schema.jsonify(song_py)


@app.route("/songpy/<id>", methods=["PUT"])
def update_song_py(id):
    song_py = Song_py.query.get(id)
    if not song_py:
        abort(404)
    old_song_py = copy.deepcopy(song_py)
    song_py.name = request.json['name']
    song_py.duration_in_min = request.json['duration_in_min']
    song_py.year = request.json['year']
    song_py.singer = request.json['singer']
    song_py.genre = request.json['genre']
    song_py.album = request.json['album']
    db.session.commit()
    return song_schema.jsonify(old_song_py)


@app.route("/songpy/<id>", methods=["DELETE"])
def delete_song_py(id):
    song_py = Song_py.query.get(id)
    if not song_py:
        abort(404)
    db.session.delete(song_py)
    db.session.commit()
    return song_schema.jsonify(song_py)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
