class Turtle:
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    @property
    def name(self):
        return self.__name


t1 = Turtle("greenTurtle", 2)
print(t1.name) # prints greenTurtle
print(t1._age) # prints 2, but shouldn't do it
# print(t1._Turtle__name)
# print(t1.__name) # 'Turtle' object has no attribute '__name'. Did you mean: 'name'?
