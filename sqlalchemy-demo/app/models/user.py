from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user_information'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class UserAddress(db.Model):
    __tablename__ = 'user_address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user_information.id'),
                        nullable=False)
    address = db.Column(db.String(120), nullable=False)
    # 一对多关系
    user = db.relationship('User', backref=db.backref('address', lazy=True))

    def __repr__(self):
        return '<UserAddress %r>' % self.address
