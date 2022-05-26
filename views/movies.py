from flask import request
from flask_restx import Resource, Namespace

from models import MovieSchema, Movie
from setup_db import db

movies_ns = Namespace("movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        if year:
            movies = Movie.query.filter(Movie.year == year).all()
        elif director_id:
            movies = Movie.query.filter(Movie.director_id == director_id)
        elif genre_id:
            movies = Movie.query.filter(Movie.genre_id == genre_id)
        else:
            movies = Movie.query.all()
        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        db.session.add(new_movie)
        db.session.commit()
        db.session.close()
        return "", 201


@movies_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = Movie.query.get(id)
        return movie_schema.dump(movie), 200

    def put(self, id):
        movie = Movie.query.get(id)
        req_json = request.json

        movie.title = req_json.get['title']
        movie.description = req_json.get['description']
        movie.trailer = req_json.get['trailer']
        movie.year = req_json.get['year']
        movie.rating = req_json.get['rating']
        movie.genre_id = req_json.get['genre_id']
        movie.director_id = req_json.get['director_id']

        db.session.add(movie)
        db.session.commit()
        db.session.close()
        return "", 204

    def delete(self, id):
        movie = Movie.query.get(id)

        db.session.delete(movie)
        db.session.commit()
        db.session.close()
        return "", 204
