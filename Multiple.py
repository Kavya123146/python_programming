#multiple
class mother:
    def parent(self):
        print("This is mother class")
class father:
    def parent1(self):
        print("This is father class")
class child(mother,father):
    def parchild(self):
        print("This is from mother & father")
ch=child()
ch.parchild()
