import os

path = input("Enter the directory path: ")

if os.path.exists(path) and os.path.isdir(path):
    all_items = os.listdir(path)
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("Only Directories:", directories)
    print("Only Files:", files)
    print("All Directories and Files:", all_items)
else:
    print("Error: The specified path does not exist or is not a directory.")
