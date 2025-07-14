from typing import List  # noqa

import sqlalchemy  # noqa

from sqlalchemy import ForeignKey, String, Table, Column, Integer, MetaData, Date, create_engine  # noqa
from sqlalchemy.ext.declarative import declarative_base  # noqa

from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship  # noqa

from typing_extensions import Annotated  # noqa

# 创建数据库连接
engine = create_engine(
    'mysql+cymysql://root:123456@localhost:3306/test_sqlalchemy', echo=True)

# 映射关系类
Base = declarative_base()

int_pk = Annotated[int, mapped_column(primary_key=True)]
string_10_required = Annotated[str, mapped_column(String(10), nullable=False)]


class NewUser(Base):
    __tablename__ = 'new_user'
    id: Mapped[int_pk]
    name: Mapped[string_10_required]
    fullname: Mapped[string_10_required]
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    # 根据情况 判断是否需要定义 是懒惰的
    address_list: Mapped[List["NewAddress"]] = relationship(
        "NewAddress", back_populates="user")


class NewAddress(Base):
    __tablename__ = 'new_address'
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey('new_user.id'))
    # 不懒惰
    user: Mapped["NewUser"] = relationship(back_populates="address_list",
                                           lazy=False)
    address: Mapped[string_10_required]


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
