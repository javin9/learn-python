from db_init import Session, Person  # noqa

session = Session()
result = session.query(Person).filter(Person.age == 17)
print(result.all())

for row in result.all():
    print(row)

print("first=")  # noqa  first 可有可无
result = session.query(Person).filter(Person.age == 17).first()
print(result)

print("one=")  # one  要求有且只有一条
result = session.query(Person).filter(Person.age == 18).one()
print(result)

print("sclar=")  # one  里面没有数据，不会报错，多了会报错
result = session.query(Person).filter(Person.age == 18).sclar()
print(result)
