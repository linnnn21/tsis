def countdown_generator(n):
    for i in range(n, -1, -1):  
        yield i  

n = int(input("Enter a number: "))
for num in countdown_generator(n):
    print(num, end=" ")
