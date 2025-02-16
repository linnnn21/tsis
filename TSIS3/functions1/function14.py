def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(lst):
    return [x for x in lst if isPrime(x)]

def unique(lst):
    return list(dict.fromkeys(lst))

name = input("Hello! What's your name? ")
print(f"Okay, {name}, enter a list of numbers separated by spaces.")

mylist = list(map(int, input("Enter numbers: ").split()))

print(f"Okay, {name}, here are your results:")
print("1) Prime numbers from list:", filter_prime(mylist))
print("2) Unique elements from list:", unique(mylist))
