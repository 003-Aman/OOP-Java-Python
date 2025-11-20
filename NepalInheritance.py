#Inheritance in python
# It is a simple concept of how places are inside places

class Country:
    country = input("Kun desh ko hau timi? ")
    def __init__(self,con,pop):
        self.Continent = con
        self.Population = pop

    def display_info(self):
        print(self.country+ " lies in the continent: "+self.Continent)
        print(self.country+" has a population of : "+ self.Population)

class State(Country):
    
    def __init__(self,con, pop, state,city):
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






#Lets do one more which is the practical inheritance that we see of Grandfather, Father and son

class GrandFather:
    Surname = "Shrestha"
    def __init__(self,name, position):
        self.GrandName = name 
        self.GPosition = position

    def display_relation(self):
        print(self.Surname+ " is the surname of my family.")
        print(self.GrandName+" is my "+self.GPosition)

class Father(GrandFather):
    def __init__(self, name, position,name1,position1):
        super().__init__(name, position)  
        self.FatherName = name1
        self.Fposition = position1

    def display_relation(self):
        super().display_relation()
        print(self.FatherName+" is my "+self.Fposition)
        print(self.FatherName+"is the son of "+self.GrandName)

class Son(Father):
    def __init__(self, name, position, name1, position1,name2,position2):
        super().__init__(name, position, name1, position1)  
        self.MyName = name2
        self.MyPosition = position2  

    def display_relation(self):
        super().display_relation()
        print("My name is "+self.MyName)
        print("I am the "+self.MyPosition+ " of"+self.FatherName )  


   

final = Town(continent,population,state,city,town,ward)
extreme = Son("Tek Bahadur","GrandFather","Lal Kumar","Father","Aman","Son")
#2 hours of code

extreme.display_relation()  
