import os
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from app.forms.user import UserForm
from app.lib.result import result
from app.models.user import db, User
# from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
# 配置数据库连接地址
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql+cymysql://root:123456@localhost:3306/flask_ddd"
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/add_user", methods=["POST"])
def create_user():
    form = UserForm()
    if form.validate_arguments():
        try:
            user = User(name=form.name.data.strip(),
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()
            # user.save()
            return result({"message": "inserted successfully"})
        except Exception as e:
            return result({}, 500, str(e))
    else:
        return form.arguments_error()


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
