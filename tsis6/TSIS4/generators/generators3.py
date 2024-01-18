def divisible_34(n):
    for i in range(n+1):
        if i % 3 == 0  and i % 4 == 0:
            yield i

num = int(input("Enter some number: "))
print(" ".join(map(str,divisible_34(num)))) #map coverts to string