from db_init import Session, NewUser, NewAddress  # noqa

session = Session()


def insert(session):
    spongebob = NewUser(
        name="ddff",
        fullname="dssdf",
        age=22,
        address_list=[NewAddress(address="sfsasdf")],
    )

    session.add(spongebob)
    session.commit()


def select_result(session):
    result = session.query(NewUser).all()

    # lazy 懒惰的模式，不会立即加载关联对象
    for row in result:
        print(row.name, row.fullname, row.age)


select_result(session)
