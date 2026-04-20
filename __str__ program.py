class display():
    def __init__(self,name,age):
        self.name=name
    def __str__(self):
        return f"{self.name}","{self.age}"
d1=display("silence")
print(d1)
