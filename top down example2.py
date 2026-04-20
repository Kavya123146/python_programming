#top down example2
#Area of Rectangle
def main():
    l,b=get_values()
    area=calculate_area(l,b)
    display(area)
def get_values():
    return 5,3
def calculate_area(l,b):
    return l*b
def display(area):
    print("Area is:",area)
main()
