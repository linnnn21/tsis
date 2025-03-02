thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")  #If there are more than one item with the specified value, the remove() method removes the first occurrence
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()  #If you do not specify the index, the pop() method removes the last item.
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because have succsesfully deleted "thislist".

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
