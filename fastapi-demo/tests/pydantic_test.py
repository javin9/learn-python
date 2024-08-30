from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int  # 必填字段
    name: str = "冰箱太凉"  # 有默认值，选填字段
    signup_ts: Optional[datetime] = None  # 无默认值 选填字段
    friends: List[int] = []  # 列表中的元素是int类型或者可以转换为int类型的字符串

    def __str__(self):
        return f"id:{self.id} -- name:{self.name}--signup_ts: {self.signup_ts} friends:{self.friends}"


external_data = {
    "id": "123",
    "name": "John Doe",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, 2, 3]
}

user = User(**external_data)

print(user)
print(user.dict())

# User(id=1, name="冰箱太凉", signup_ts=datetime.today(), friends=[1, "ni", 3])
try:
    User(id=1, name="冰箱太凉", signup_ts=datetime.today(), friends=[1, "ni", 3])
except Exception as e:
    print(e.json())

print(user.dict())
print(user.json())
print(user.copy())
print(
    User.parse_raw(
        '{"id":123,"name":"John Doe","signup_ts":"2017-06-01T12:22:00","friends":[1,2,3]}'
    ))
print(User.parse_obj(external_data))
print(User.__fields__.keys())
