import re
text = str(input("Enter a string: "))
match = re.findall(r'[A-Z][a-z]+' , text) #first letter uppercase other lowercase
print(match)