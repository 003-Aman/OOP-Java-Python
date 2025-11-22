class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(self.brand + " " + self.model + ": A phone has a job of taking calls.")

class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(self.brand + " " + self.model + ": A laptop has a task of managing things.")

class Watch:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(self.brand + " " + self.model + ": A watch has a task of showing time.")


# Create objects
p1 = Phone("Apple", "17 pro max")
l1 = Laptop("Apple", "Macbook m4")
w1 = Watch("Apple", "Series1")

# Loop through and call info().THIS ON IS INTERSTING HAVE A LOOK ON IT. USE LOOPING BETTER
for i in (p1, l1, w1):
    i.info()

#INHERITANCE CLASS POLYMORPHISM
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle): # FOR CLASS CAR THE MOVE FUNCTION WILL PRINT MOVE SINCE IT DOESNT HAVE ANYTHING OF ITS OWN . IT WILL INHERIT IT . BUT FOR THE OTHERS ITS NOT THE SAME BECAUSE THEY HAVE THE MOVE FUNCTION OF THEIR OWN
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()