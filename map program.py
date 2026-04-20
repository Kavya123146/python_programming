#lambda functions
#example1
nums=[1,2,3,4,5,6]
print(list(map(lambda x:x*2,nums)))
#example2
nums=[2,3,5,4,8,9,10]
print(list(filter(lambda x:x%2!=0,nums)))
#example3
from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda x,y:x+y ,l))
