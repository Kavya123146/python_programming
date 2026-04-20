#polymorphism
class vechicles:
    def move(self):
        print("vechicles moves")
class car(vechicles):
    def move(self):
        print("car used to drive")
class boat(vechicles):
    def move(self):
        print("boat is sails in river")
v1=car()
v1.move()
v2=boat()
v2.move()
