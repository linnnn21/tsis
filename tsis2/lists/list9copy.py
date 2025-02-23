thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)  #use the built-in method list()
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist[:] #by using the : (slice) operator
print(mylist)