class ClassA():
    def __init__(self):
        self.name = "class A"

    def sayHi(self):
        print(f'{self.name} says hi')


class ClassB(ClassA):
    def __init__(self):
        self.name = "class B"
