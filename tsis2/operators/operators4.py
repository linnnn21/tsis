#identify
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)  
print(x is not y)
print(x != y) 

#membership operators
x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("banana"not in x)
