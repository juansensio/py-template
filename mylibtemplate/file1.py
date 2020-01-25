class ClassA():
    """ hola """

    def __init__(self):
        """ que pasa """
        self.name = "class A"

    def sayHi(self):
        """ say his """
        print(f'{self.name} says hi')


class ClassB(ClassA):
    """ eiso """

    def __init__(self):
        self.name = "class B"
