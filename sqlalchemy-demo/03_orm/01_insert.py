import sqlalchemy  # noqa

from sqlalchemy import ForeignKey, String, Table, Column, Integer, MetaData, Date, create_engine  # noqa
from sqlalchemy.ext.declarative import declarative_base  # noqa

from sqlalchemy.orm import sessionmaker  # noqa

from db_init import Session, Person  # noqa

# 创建一个session对象
session = Session()

# p = Person(name='xiaoming', age=18, birthday='2000-01-01')
# session.add(p)

# 批量插入
person_list = [
    Person(name='zhangsan1', age=38, birthday='2080-01-01'),
    Person(name='wangwu2', age=17, birthday='2003-01-01'),
    Person(name='maliu', age=17, birthday='2003-01-01')
]
session.add_all(person_list)

session.commit()
