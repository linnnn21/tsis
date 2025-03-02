file_path = input("Enter the text file path: ")

try:
    line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
    print("Number of lines:", line_count)
except FileNotFoundError:
    print("Error: File not found.")
