from sqlalchemy import select  # noqa
from db_init import engine, employee__table, deparment_table  # noqa

# with engine.connect() as connection:
#     join_sql = employee__table.join(
#         deparment_table,
#         employee__table.c.department_id == deparment_table.c.id)

#     select_query = select(join_sql).where(
#         deparment_table.c.name == 'Engineering')
#     result = connection.execute(select_query)
#     data_list = result.fetchall()
#     print("join=", data_list)

# with engine.connect() as connection:
#     join_sql = employee__table.join(
#         deparment_table,
#         employee__table.c.department_id == deparment_table.c.id)

#     select_query = select(employee__table).select_from(join_sql).where(
#         deparment_table.c.name == 'Engineering')

#     result = connection.execute(select_query)
#     data_list = result.fetchall()
#     print("join=", data_list)

# with engine.connect() as connection:
#     join_sql = employee__table.join(
#         deparment_table,
#         employee__table.c.department_id == deparment_table.c.id)
#     select_query = select(deparment_table).select_from(join_sql).where(
#         employee__table.c.name == 'David')
#     result = connection.execute(select_query)
#     data_list = result.fetchall()
#     print(data_list)

with engine.connect() as connection:
    select_query = employee__table.select().where(
        employee__table.c.name == 'David').join(
            deparment_table,
            employee__table.c.department_id == deparment_table.c.id)
    print(connection.execute(select_query).fetchall())
