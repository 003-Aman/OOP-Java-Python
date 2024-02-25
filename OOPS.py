class Coding:
    def __init__(self,level,skill):
        self.year = level
        self.skill = skill

    def display_resume(self):
        print("COLLEGE YEAR:"+ self.year)
        print("SKILL EXP: "+self.skill) 

c1 = Coding("Freshman","ML and AI") 
c1.display_resume()          