class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour =  colour
        self.age = 1
        self.energy = 100

    def make_noise(self):
        print('Animal made a noise!')

class Cat(Animal):
    def make_noise(self):
        print('Meow!')

    def scratch(self):
        print('You have been scratched!')

sid = Cat('Sid', 'Black')
sid.make_noise()