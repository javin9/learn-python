import sqlalchemy  # noqa

from sqlalchemy import ForeignKey, String, Table, Column, Integer, MetaData, Date, create_engine  # noqa
from sqlalchemy.ext.declarative import declarative_base  # noqa

from sqlalchemy.orm import sessionmaker  # noqa

# 创建数据库连接
engine = create_engine(
    'mysql+cymysql://root:123456@localhost:3306/test_sqlalchemy', echo=True)

# 映射关系类
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(2048), nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    birthday = Column(Date, nullable=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
