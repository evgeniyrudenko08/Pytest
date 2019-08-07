#from Lib.python_lab_second import First

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name + " jump")

dog = Animal("Pit", 1)
print (dog.name, dog.age)
dog.sit()

class Cat(Animal):
    def __init__(self, name, age, gender):
        print(name,'has four legs and', age, 'years old', 'and Gender is', gender)
        super(Cat, self).__init__(age, gender)

c = Cat('Pili', 4, 'g')
