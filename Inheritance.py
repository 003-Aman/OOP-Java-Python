class HumanBeing:
    def __init__(self,sex,ethnicity):
        self.Gender =sex
        self.Ethnicity = ethnicity

    def display_human(self):
        print("Details: "+self.Gender+" "+self.Ethnicity)
        print("this is the display_human() of the original class")

class Profession(HumanBeing):
    def display_human(self):
        print(self.Gender,self.Ethnicity) #value changes now according to the parametric value
        print("this is the display_human() function of the Profession class")    

o1= HumanBeing("Male","Asian")
o2=Profession("Female","Black") #doesnt have a parameterized constructor so nothing passed
#xuttai xuttai object garna manlayo vane yei ho natra eutai garxu vanyo vane chai super.__init__()
o1.display_human()
o2.display_human()              