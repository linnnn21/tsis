file_path = input("Enter the file path: ")
my_list = ["Apple", "Banana", "Cherry", "Date"]

with open(file_path, 'w') as file:
    for item in my_list:
        file.write(item + '\n')

print("List written to file.")
