import sqlalchemy  # noqa

from sqlalchemy import ForeignKey, String, Table, Column, Integer, MetaData, create_engine

# 创建数据库连接
engine = create_engine(
    'mysql+cymysql://root:123456@localhost:3306/test_sqlalchemy', echo=True)
# 连接数据库
connection = engine.connect()

meta = MetaData()

deparment_table = Table(
    "deparment",
    meta,
    Column("id", Integer, primary_key=True, unique=True),
    Column("name", String(2048), nullable=False),
    Column("department_code", String(2048), nullable=False),
    Column("description", String(2048), nullable=False),
)

employee__table = Table(
    "employee",
    meta,
    Column("id", Integer, primary_key=True, unique=True),
    Column("department_id", ForeignKey("deparment.id"), nullable=False),
    Column("name", String(2048), nullable=False),
    Column("age", Integer, nullable=False),
)

# 创建表
meta.create_all(engine)
