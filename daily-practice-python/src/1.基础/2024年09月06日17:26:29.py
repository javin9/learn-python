import sys

print(sys.maxunicode)

print(range(sys.maxunicode))

text = 'Hello World'
new_text = text.center(20, '*')
print(new_text)

name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

formatted_string = "My name is {0} and I am {1} years old.".format(name, age)
print(formatted_string)

formatted_string = "My name is {name} and I am {age} years old.".format(
    name="Bob", age=25)
print(formatted_string)

pi = 3.141592653589793
formatted_string = "Pi to three decimal places: {0:.3f}".format(pi)
print(formatted_string)

percentage = 0.85
formatted_string = "Success rate: {:.2%}".format(percentage)
print(formatted_string)
# 输出: Success rate: 85.00%

person = {'name': 'David', 'age': 40}
formatted_string = "Name: {0[name]}, Age: {0[age]}".format(person)
print(formatted_string)

# vars
s = '{name} has {n} messages.'
name = 'Guido'
n = 37
result = s.format_map(vars())
print(result)

#


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = "{name} is {age} years old."
res = s.format_map(vars(User('Alice', 25)))
print(res)
