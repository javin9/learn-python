import sqlalchemy

# print(sqlalchemy.__version__)

from sqlalchemy import ForeignKey, String, Table, Column, Integer, MetaData, create_engine
# import time

print(f'sqlalchemy version is {sqlalchemy.__version__}')
# 创建数据库连接
engine = create_engine(
    'mysql+cymysql://root:123456@localhost:3306/test_sqlalchemy', echo=True)
# 连接数据库
connection = engine.connect()
print("连接数据库成功")

meta = MetaData()
students = Table(
    "user_account",
    meta,
    Column("id", Integer, primary_key=True, unique=True),
    Column("first_name", String(10), nullable=False),
    Column("last_name", String(10), nullable=False),
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

# insert_zhang = students.insert().values(first_name="hu_tom", last_name="tom_2")

# 批量插入数据
s_insert = students.insert()
with engine.connect() as connection:
    connection.execute(s_insert, [{
        "first_name": "hu_tom_1",
        "last_name": "tom_2_4"
    }, {
        "first_name": "hu_tom_3",
        "last_name": "tom_2_1"
    }])
    connection.commit()

# time.sleep(10000)
# 关闭连接，销毁引擎
connection.close()
engine.dispose()

print("关闭连接，销毁引擎")
