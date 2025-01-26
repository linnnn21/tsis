thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Remove a random item by using the pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)