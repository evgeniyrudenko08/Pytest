from abc import ABC, abstractmethod
import collections


class AbstractAnimal(ABC):
    pass

    @abstractmethod
    def make_sound(self):
        print(cls)
    @abstractmethod
    def eat(object):
        print(object)

class Dog(AbstractAnimal):
    def make_sound(self):
           print(self)

    def eat(self):
           print(self)

    def pr():
        a = Dog.eat(["Pootato", "Tomato"])
        b = Dog.eat("yyy")
        c = Dog.make_sound('Gav')

Dog.pr()

class Cat(AbstractAnimal):
    def make_sound(self):
        print(self)

    def cc():
        a = Cat.make_sound("Myau")
        print(a)
Cat.cc()








