def even_number_generator(n):
    for i in range(0, n + 1, 2):  
        yield str(i)  

n = int(input("Enter a number: "))
print(",".join(even_number_generator(n)))
