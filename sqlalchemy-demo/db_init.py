import sqlalchemy

from sqlalchemy import ForeignKey, String, Table, Column, Integer, MetaData, create_engine

print(f'sqlalchemy version is {sqlalchemy.__version__}')
# 创建数据库连接
engine = create_engine(
    'mysql+cymysql://root:123456@localhost:3306/test_sqlalchemy', echo=True)
# 连接数据库
connection = engine.connect()

meta = MetaData()

user_table = Table(
    "user_account",
    meta,
    Column("id", Integer, primary_key=True, unique=True),
    Column("first_name", String(10), nullable=False),
    Column("last_name", String(10), nullable=False),
    Column("age", Integer, nullable=False),
)

address_table = Table(
    "address",
    meta,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("address", String(100), nullable=False, unique=True),
)

# 创建表
meta.create_all(engine)
