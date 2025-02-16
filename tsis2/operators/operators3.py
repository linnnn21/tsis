#logical
x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4) # returns True because one of the conditions are true

x = 5
print(not(x > 3 and x < 10))  # returns False because not is used to reverse the result