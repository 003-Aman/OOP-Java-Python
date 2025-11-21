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

# Loop through and call info()
for i in (p1, l1, w1):
    i.info()
