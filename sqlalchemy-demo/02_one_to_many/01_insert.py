import random
from db_init import engine, employee__table  # noqa

# with engine.connect() as connection:
#     insert_sql = deparment_table.insert()
#     connection.execute(insert_sql, [
#         {
#             "name": "Engineering",
#             "department_code": "ENG",
#             "description":
#             "Responsible for product development and innovation."
#         },
#         {
#             "name": "Sales",
#             "department_code": "SAL",
#             "description":
#             "Responsible for selling company products and services."
#         },
#         {
#             "name": "Marketing",
#             "department_code": "MKT",
#             "description":
#             "Responsible for promoting company products and brand."
#         },
#         {
#             "name": "Finance",
#             "department_code": "FIN",
#             "description": "Responsible for financial planning and management."
#         },
#         {
#             "name":
#             "Human Resources",
#             "department_code":
#             "HR",
#             "description":
#             "Responsible for managing employee relations and welfare."
#         },
#         {
#             "name":
#             "Customer Support",
#             "department_code":
#             "CS",
#             "description":
#             "Responsible for assisting customers with product inquiries and issues."
#         },
#         {
#             "name":
#             "Research and Development",
#             "department_code":
#             "R&D",
#             "description":
#             "Responsible for scientific research and product innovation."
#         },
#         {
#             "name":
#             "Operations",
#             "department_code":
#             "OPS",
#             "description":
#             "Responsible for managing day-to-day business operations."
#         },
#         {
#             "name":
#             "Information Technology",
#             "department_code":
#             "IT",
#             "description":
#             "Responsible for managing company's IT infrastructure and systems."
#         },
#         {
#             "name":
#             "Quality Assurance",
#             "department_code":
#             "QA",
#             "description":
#             "Responsible for ensuring product quality and compliance with standards."
#         },
#     ])
#     connection.commit()
#     connection.close()
#     engine.dispose()

# 真实的员工姓名和年龄数据（示例）
employee_names = [
    "Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah",
    "Ian", "Jack", "Katie", "Liam", "Mia", "Noah", "Olivia", "Patrick",
    "Quinn", "Rachel", "Sam", "Taylor"
]
min_age = 20
max_age = 60

# 生成模拟数据
mock_data = []
for name in employee_names:
    department_id = random.randint(1, 10)
    age = random.randint(min_age, max_age)
    mock_data.append({
        "department_id": department_id,
        "name": name,
        "age": age
    })

# 插入数据到数据库
with engine.connect() as connection:
    for data in mock_data:
        connection.execute(employee__table.insert(), data)
    connection.commit()
    connection.close()
