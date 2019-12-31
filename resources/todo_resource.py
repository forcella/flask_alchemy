from flask import jsonify
from flask_restful import Resource

from domain.model.todo import Todo


class TodoResource(Resource):

    def get(self, _id: int):
        return jsonify(Todo(_id=_id, task="Estudar PY", status="DOING"))

    def post(self):
        pass


class TodoListResource(Resource):

    def get(self, user_id: int):
        return {"user": "Usuario", "todos:": [Todo(_id=66, task="Estudar PY", status="DOING")]}
