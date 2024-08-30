from db_init import Session, Person  # noqa
# 创建事务
session = Session()

result = session.query(Person).filter(Person.age == 18).update(
    {Person.name: "dongchang"})
session.commit()
