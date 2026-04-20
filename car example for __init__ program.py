class car:
    def __init__(self,carname,model,cost,colour):
        self.carname=carname
        self.model=model
        self.cost=cost
        self.colour=colour
    def display(self):
        print("carname is:",self.carname)
        print("car model:",self.model)
        print("car cost:",self.cost)
        print("car colour:",self.colour)
c=car("Thar","new",100000,"white")
c.display()
    
        
        
