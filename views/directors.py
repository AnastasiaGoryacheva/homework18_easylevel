from flask_restx import Resource, Namespace

from models import DirectorSchema, Director

directors_ns = Namespace("directors")

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = Director.query.all()
        return directors_schema.dump(directors), 200


@directors_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id):
        director = Director.query.get(id)
        return director_schema.dump(director), 200
