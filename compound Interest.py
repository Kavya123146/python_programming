#compound Interest:
p=float(input("Enter pricipal amount:"))
r=float(input("Enter Rate of interest:"))
t=float("Enter Time(in years):")
amount=p*(1+r/100)**t
ci=amount-p
print("Total Amount=",amount)
print("compound Interest=",ci)
