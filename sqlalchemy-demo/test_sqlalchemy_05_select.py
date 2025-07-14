from db_init import engine, meta, user_table, address_table  # noqa

# 查询数据，没有都放到内存中
with engine.connect() as connection:
    query = user_table.select()
    data_list = connection.execute(query)

    # 迭代器
    for row in data_list:
        print(f'first_name={row.first_name},last_name={row.last_name}')

    connection.close()
    engine.dispose()

# 全部数据，fetchall 都放到了内存中
with engine.connect() as connection:
    query_sql = user_table.select()
    result = connection.execute(query_sql)
    data_list = result.fetchall()
    print("fetchall=", data_list)

# 条件查询，只要第一条数据
with engine.connect() as connection:
    query_sql = user_table.select().where(
        user_table.c.first_name == 'zhang').where(
            user_table.c.last_name == 'san')
    result = connection.execute(query_sql)
    data_list = result.fetchone()
    print("where+fetchone=", data_list)

with engine.connect() as connection:
    query_sql = user_table.select().limit(1)
    result = connection.execute(query_sql)
    data_list = result.fetchall()
    print("limit=", data_list)
