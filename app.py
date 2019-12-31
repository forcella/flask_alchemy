from flask import Flask
from flask_restful import Api

from resources.todo_resource import TodoResource

app = Flask(__name__)
app.secret_key = 'super_secret'

api = Api(app)

api.add_resource(TodoResource, "/todos/<string:_id>")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
