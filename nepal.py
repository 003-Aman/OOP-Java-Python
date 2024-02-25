#Inheritance in python
class Country:
    country = input("Kun desh ko hau timi? ")
    def __init__(self,con,pop):
        self.Continent = con
        self.Population = pop

    def display_info(self):
        print(self.country+ " lies in the continent: "+self.Continent)
        print(self.country+" has a population of : "+ self.Population)

class State(Country):
    def __init__(self, con, pop,state,city):
        super().__init__(con, pop)  
        self.State = state
        self.City = city

    def display_info(self):
        super().display_info() 
        print(self.State + " lies inside of "+self.country)
        print(self.City+ " is the place I live inside "+self.State)


class Town(State):
    def __init__(self, con, pop, state, city,town,ward):
        super().__init__(con, pop, state, city)
        self.Town = town
        self.WardNo = ward

    def display_info(self):
        super().display_info()
        print(self.Town+" is where I live in inside "+ self.City)
        print(self.WardNo+" is the ward no. where I live in inside "+ self.Town)    


continent = input("Kun continent ma basxas :")
population = input("Afno desh ko jansankhya hala babu: ")
state = input("Kun ho state chai : ")
city= input("What is the name of your city: ")
town = input("Basne thau ko naam chai k thyo: ")
ward = input("kun oda bhitra parthyo lekh nepal ko bhane natra street no. : ")
print("------------------------------------------------------")
print("------------------------------------------------------")

final = Town(continent,population,state,city,town,ward)
final.display_info()