# a default constructor is one that doesnt take a parameter 

class University:
    def __init__(self):
        self.name = 'Augustana College' # this means while creating an object we dont need to put in a value and the default value for self.name will be "augustana college" until we chang it
        self.location ="Illinois"

    def display_college_info(self):
        print("Aman Shrestha studied at "+ self.name+' of ' +self.location)   

Uni = University()#just creating an object without a parameter
Uni.display_college_info()         
        

# a parameterized constructor will wait for the user to give a value when the object is created, but still can have some default values

class America:
    def __init__(self,continent,president):
        self.powerful = True # this will be default when the object is made using this class
        self.Continent = continent # this means I am waiting for the user(me) to put in the value in the continent parameter when the object is made using the America class
        self.President = president

    def display_info(self):
        print("The statement of america being a powerful country is : "+str(self.powerful)+" "+ self.Continent+" "+ self.President)

continent = input("What is the continent of your choice :")
president = input("Who is the president of America today? ")

A1 = America(continent, president) # object A1 is created using the class America and the value is given as an input
# i couldve just given the value but I made it intersting
A1.display_info()