from flask_restx import Resource, Namespace

from models import GenreSchema, Genre

genres_ns = Namespace("genres")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = Genre.query.all()
        return genres_schema.dump(genres), 200


@genres_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id):
        genre = Genre.query.get(id)
        return genre_schema.dump(genre), 200
