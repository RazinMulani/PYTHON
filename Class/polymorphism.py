# PolyMorphism:
# In Class More Than One Method having same name with different parameter is called method



class dog:
    def __init__(self,sound):
        self.sound = sound
    def display(self):
        print("Dog Sound IS:",self.sound)

class cat:
    def __init__(self,sound):
        self.sound = sound
    def display(self):
        print("Cat Sound is:",self.sound)
        
class animal(cat,dog):
    def __init__(self,sound):
        self.sound = sound
    def display(self):
        print("Animal Sounds",self.sound)
o = animal("Animal Sound")
o1 = dog("Barks")
o2 = cat("Mew")

o.display()
o1.display()
o2.display()

