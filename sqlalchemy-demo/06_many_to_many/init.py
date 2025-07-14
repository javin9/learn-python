from typing import List
from sqlalchemy import (Column, ForeignKey, Integer, String, Table,
                        create_engine)
from sqlalchemy.orm import (declarative_base, relationship, Mapped, Session,
                            registry)

# 使用新的映射声明注册方式
mapper_registry = registry()
Base = mapper_registry.generate_base()

# 关联表
user_role_association_table = Table(
    'user_role_association', Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('role_id', ForeignKey('roles.id'), primary_key=True))


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(258))
    roles: Mapped[List['Role']] = relationship(
        'Role', secondary=user_role_association_table, back_populates='users')


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(258))
    users: Mapped[List['User']] = relationship(
        'User', secondary=user_role_association_table, back_populates='roles')


engine = create_engine(
    'mysql+cymysql://root:123456@localhost:3306/test_sqlalchemy', echo=True)

# 创建所有表
Base.metadata.create_all(engine)

# 创建session
session = Session(engine)

# 示例：添加用户和角色
new_user = User(name='Alice')
new_role = Role(name='Admin')
new_user.roles.append(new_role)

session.add(new_user)
session.commit()

# 查询用户
alice = session.query(User).filter_by(name='Alice').first()
print(alice.name)
for role in alice.roles:
    print(role.name)

session.close()
