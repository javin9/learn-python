from flask import Flask, request

from flask_restful import Api, Resource

from app.TodoSimple import TodoSimpleResource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}


class TodoSimple(Resource):
    todos = {
        "1": "task1",
        "2": "task2",
    }

    def get(self, id):
        print(request.args["page"])
        return {id: self.todos[id]}

    def post(self, id):
        json_data = request.get_json()
        json_data.get("data")
        self.todos[id] = json_data.get("data")  # request.form['data']
        return {id: self.todos[id]}


api.add_resource(HelloWorld, '/')
# api.add_resource(TodoSimpleResource, '/simple/<id>')
api.add_resource(TodoSimpleResource, '/simple')

if __name__ == '__main__':
    app.run(debug=True, port=3333)
