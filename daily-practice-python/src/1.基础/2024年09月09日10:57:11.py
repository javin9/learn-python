#
from decimal import Decimal
import random

round(1.23, 1)
print(round(1.23434, 3))

print(round(1.5))
print(round(2.5))
x = 1.23456
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print('value is {:0.3f}'.format(x))

a = 2.1
b = 4.2
c = a + b
print(c)

print(round(c, 1))
print(round(c, 3))
print(Decimal('1.1') + Decimal('1.3'))
print(Decimal(1.1 + 2.2))

#
values = [1, 2, 3, 4, 5, 6, 2, 5, 6, 7]

print(random.choice(values))
print(random.choices(values, k=2))
print(random.sample(values, 2))
