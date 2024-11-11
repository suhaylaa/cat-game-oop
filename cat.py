class Cat:
    # The constructor
    # - The constructor will create a cat for us in code
    # - To create a cat, we need a given_name & given_colour
    # - self is the cat that we are creating.
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
        print()
        self.energy += 20
        self.age += 0.1
    
    def showStats(self):
        print(f"This is {self.name}'s stats.")
        print(f"Your Cat's age is {self.age}.") 
        print(f"Your Cat's energy level is {self.energy}.")
        print(f"Your cat's energy level is {self.intelligence}.")
        print(f"Your Cats's weight is {self.weight}.")