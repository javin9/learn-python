# import sqlalchemy

# print(sqlalchemy.__version__)

from sqlalchemy import create_engine, __version__

print(f'sqlalchemy version is {__version__}')
# 创建数据库连接
engine = create_engine('mysql+cymysql://root:123456@localhost:3306/flask_ddd',
                       echo=True)
# 连接数据库
connection = engine.connect()
print("连接数据库成功")
# 关闭连接，销毁引擎
connection.close()
engine.dispose()

print("关闭连接，销毁引擎")
