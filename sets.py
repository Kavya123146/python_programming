#sets
#1.union
a={1,2,3}
b={4,5,6}
print("The union is",a.union(b))
#intersection
a={1,2,3}
b={2,3,4,5}
print("The intersection is using &",a&b)
#difference
a={1,9,8,7}
b={2,1,9,5}
print("The difference is using -",a-b)
#symetric difference
print("The difference is using ^",a^b)
