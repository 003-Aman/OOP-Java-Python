class Coding:
    def __init__(self,level,skill):
        self.year = level
        self.skill = skill

    def display_resume(self):
        print("COLLEGE YEAR:"+ self.year)
        print("SKILL EXP: "+self.skill) 

c1 = Coding("Freshman","ML and AI") 
c1.display_resume() 

class Addition:
    
    def __init__(self,first,second):
        self.first = first
        self.second = second


    def answer(self):
        return (self.first + self.second)
    
calc = Addition(40,48)
message = calc.answer()  
print(message)  
        
