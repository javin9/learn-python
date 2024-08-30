import datetime

import sqlalchemy  # noqa

from sqlalchemy import ForeignKey, String, Table, Column, Integer, MetaData, Date, create_engine  # noqa
from sqlalchemy.ext.declarative import declarative_base  # noqa

from sqlalchemy.orm import sessionmaker, Mapped, mapped_column  # noqa

from typing_extensions import Annotated  # noqa

# 创建数据库连接
engine = create_engine(
    'mysql+cymysql://root:123456@localhost:3306/test_sqlalchemy', echo=True)

# 映射关系类
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)


# 定义一个新的类型，用于表示主键，这样可以避免重复定义
int_pk = Annotated[int, mapped_column(primary_key=True)]
timestamp_column = Annotated[
    datetime.datetime,
    mapped_column(nullable=False, server_default=sqlalchemy.func.now())]


class Order(Base):
    __tablename__ = 'order'
    id: Mapped[int_pk]
    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.id'))
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    create_time = Mapped[timestamp_column]


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
