import os

path = input("Enter the path to check: ")

if os.path.exists(path):
    print("Path exists:", True)
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
else:
    print("Path exists:", False)
