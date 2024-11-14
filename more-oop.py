class device:
   def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name

   def powerON(self):
       print(f"Your {self.name} has been powered on!")


class Comp(device):
    
   def powerON(self):
       print("Your computer has been powered on!")

   def compute(self):
       print("Your computer is computing ...")
   
   def playGAME(self):
       print("Your computer has started a game!")

   laptop = Comp('12','20',"laptop")
   laptop.monitorON()

class Vehicle:
   def __init__(self,name,speed,size):
        self.name =  name
        self.speed = speed
        self.size = size

   def switchON(self):
       print(f"Your {Vehicle.name} has switched on!")

   def drive(self):
       print(f"Your {Vehicle.name} is in drive")
       
   def fix(self):
       print(f"Your {Vehicle.name} is being fixed")

class car(Vehicle):
    
   def switchON(self):
       print(f"Your {car.name} has switched on!")

   def drive(self):
       print(f"Your {car.name} is in drive")
       
   def fix(self):
       print(f"Your {car.name} is being fixed")

   def makeNoise(self):
       print("Vroom")
