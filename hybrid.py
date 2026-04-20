#Hybrid inheritence
class Animal:
    def make_sound(self):
        print("Animals make sounds")
class mammal(Animal):
    def make_sound(self):
        print("mammals make sound")
class Bird(Animal):
    def make_sound(self):
        print("Birds do the sounds")
class Bat(mammal,Bird):
    pass
obj=Bat()
obj.make_sound()
