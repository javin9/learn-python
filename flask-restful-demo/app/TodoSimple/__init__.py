from flask import request
from flask_restful import Resource


class TodoSimpleResource(Resource):
    todos = {
        "1": "task1",
        "2": "task2",
    }

    def get(self):
        print(request.args["page"])
        return {id: self.todos[id]}

    def post(self):
        json_data = request.get_json()
        id = json_data.get("id")
        self.todos[id] = json_data.get("data")  # request.form['data']
        return {id: self.todos[id]}
