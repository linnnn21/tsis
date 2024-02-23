import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("Path exists:", True)
    print("Directory portion:", os.path.dirname(path))
    print("Filename portion:", os.path.basename(path))
else:
    print("Path exists:", False)
