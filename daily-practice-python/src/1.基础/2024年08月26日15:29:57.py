from collections import namedtuple

tuple_data = (1, 2, 3, 4, 5)

Point = namedtuple("Point", ["x", "y", "z", "a", "b"])
pp = Point(*tuple_data)

print(pp.x, pp.y, pp.z, pp.a, pp.b)
