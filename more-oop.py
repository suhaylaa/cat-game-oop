
class Employee:

    def __init__(self,name,DOB,role,salary):
      self.name = name
      self.DOB = DOB
      self.salary = salary
      self.role = role

    def increase_salary(self):
       print("Your salary has been increased")
       self.salary = self.salary * 1.05
    
    def calculate_age(self):
       Yage = self.age[6:] 
       age = 2024 - Yage
       self.age = age
    
class Manager:
   
    def __int__(self,name,role,salary,bonus,DOB):
      self.name = name
      self,role = role
      self.salary = salary
      self.bonus = bonus
      self.DOB = DOB

    def increase_salary(self):
        print("Your salary has been increased")
        self.salary = self.salary * 1.1

    def calculate_age(self):
       Yage = int(self.age[6:]) 
       age = 2024 - Yage
       self.age = age
       print(self.age)

    def increase_bonus(self):
       print("Your bonus has been increased")
       self.bonus = self.bonus *1.1

name = input("Enter a name: ")
role = input("Enter your role: ")
salary = int(input("enter your salary: "))
bonus = int(input("Enter your bonus: "))
DOB = input("Enter your date of birth. dd/mm/yyyy: ")
my_manager = Manager(name,role,salary,bonus,DOB)

   

