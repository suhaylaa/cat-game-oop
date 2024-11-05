class Cat:
    # The constructor
    # - The constructor will create a cat for us in code
    # - To create a cat, we need a given_name & given_colour
    # - self is the cat thtat we are creating.
    def __init__(self, given_name, given_colour):
        #name attribute
        self.name = given_name
        #colour attribute 
        self.colour = given_colour
        self.age = 1 
        self.energy = 50
        self.intelligence = 5
        self.weight = 5
    def train(self):
        print(f"{self.name}is training...")
        self.energy -= 5
        self.intelligence += 1
        self.age += 0.1
    
    def feed(self):
        print(f"{self.name}is eating...")
        self.energy += 10
        self.weight += 1
        self.age += 0.1
    
    def play(self):
        print(f"{self.name} is playing...")
        self.energy -= 10
        self.weight -= 0.5
        self.age += 0.1

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy += 20
        self.age += 0.1