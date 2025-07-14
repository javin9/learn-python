from db_init import engine, meta, user_table, address_table  # noqa
from sqlalchemy.sql import and_, or_  # noqa

# 条件查询，只要第一条数据
# with engine.connect() as connection:
#     query_sql = user_table.select().where(
#         user_table.c.first_name == 'zhang').where(
#             user_table.c.last_name == 'san')
#     result = connection.execute(query_sql)
#     data_list = result.fetchone()
#     print("where+fetchone=", data_list)

with engine.connect() as connection:
    update_sql = user_table.update().values(first_name='zheng').where(
        user_table.c.age == 88)
    result = connection.execute(update_sql)
    connection.commit()
    # print(result.rowcount)
    connection.close()
    engine.dispose()
