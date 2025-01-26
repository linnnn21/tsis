class myclass():
  def __len__(self):
    return 0  #If __len__ returns 0, the object evaluates as False.

myobj = myclass()
print(bool(myobj))