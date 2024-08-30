import json
from flask import jsonify


def result(data=None, code=200, msg=None):
    if data is None:
        data = {}
    if msg is None:
        msg = "success"

    data_json_str = json.dumps(data,
                               ensure_ascii=False,
                               default=lambda obj: obj.__dict__)
    data_json_dict = json.loads(data_json_str)

    return jsonify({"code": code, "data": data_json_dict, "msg": msg})
