#set methods
#add
firstset=["East","west","north"]
firstset.add("south")
print(firstset)

#remove
firstset=["East","west","north,south"]
firstset.remove("south")
print(firstset)

#discard
firstset=["East","west","north"]
firstset.discard("west")
print(firstset)

#pop
firstset=["East","west","north"]
firstset.pop("south")
print(firstset)

#len
firstset=["East","west","north","southh"]
print(len(firstset))

#copy
firstset=["East","west","north"]
firstset.copy()
print(firstset)
