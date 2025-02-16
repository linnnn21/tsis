def squares_generator(a, b):
    for i in range(a, b + 1): 
        yield i ** 2 

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
for num in squares_generator(a, b):
    print(num, end=" ") 
