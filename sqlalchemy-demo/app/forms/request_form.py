from flask import request
from wtforms import Form
import wtforms_json  # noqa

from app.lib.result import result
# https://blog.csdn.net/make_progress/article/details/131038714
# class RequestForm(Form):
#     #
#     def __init__(self):
#         if "application/json" in request.headers.get("Content-Type"):
#             data = request.get_json()
#             args = request.args.to_dict()
#             super(RequestForm, self).__init__(data=data, **args)
#         else:
#             self.data = request.form.to_dict()
#             args = request.args.to_dict()
#             super(RequestForm, self).__init__(data=self.data, **args)

#     def validate_arguments(self):
#         valid = super(RequestForm, self).validate()
#         if not valid:
#             raise self.arguments_error()
#         return self.validate()

#     def arguments_error(self):
#         return result(data=self.errors, code=400, msg="参数错误")


class RequestForm(Form):

    def __init__(self):
        data = request.get_json()
        args = request.args.to_dict()
        super(RequestForm, self).__init__(data=data, **args)

    def validate_arguments(self):
        valid = super(RequestForm, self).validate()
        if not valid:
            raise self.arguments_error()
        return self.validate()

    def arguments_error(self):
        return result(data=self.errors, code=400, msg="参数错误")


# class JsonForm(Form):

#     @classmethod
#     def validate_arguments(cls):
#         wtforms_json.init()
#         form = cls.from_json(request.get_json())
#         valid = form.validate()
#         if not valid:
#             raise form.arguments_error()
#         return form

#     def arguments_error(self):
#         return result(data=self.errors, code=400, msg="参数错误")
