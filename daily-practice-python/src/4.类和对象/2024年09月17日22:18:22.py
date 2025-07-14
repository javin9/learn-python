class Person:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name}, I am {self.age} years old.')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    def __repr__(self) -> str:
        return f'Person({self.name!r}, {self.age!r})'


p1 = Person('John', 20)
p1.say_hello()

print(p1)
