#square number or not
import math
n=int(input("Enter a number:"))
root=math.isqrt(n)
if root*root==n:
    print("perfect square")
else:
    print("Not a perfect square")
#another way
n=int(input("Enter a number:"))
root=int(n**0.5)
