class Animal(object):
    def run(self):
        print("animal is running")


class Dog(Animal):
    pass


class Cat(Animal):
    def run(self):
        print("cat is running")


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())
run_twice(Cat())

print(type(Cat()))
