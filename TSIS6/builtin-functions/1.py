def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num 

    return result 

numbers = list(map(int,input("Enter some numbers: ").split()))
result = multiply_list(numbers)
print("Result: ", result)
