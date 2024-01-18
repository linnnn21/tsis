x = lambda a,b : a*b 
print(x(5,6))

x = lambda a,b,c : a+b+c
print(x(5,6,2))

def myfunc(n):
  return lambda a : a * n
doubler = myfunc(2)
print(doubler(11))