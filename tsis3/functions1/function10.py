def unique(list):
    new = []
    for x in list:
        if x not in new:
            new.append(x)
    return new
list = list(map(int, input("numbers: ").split()))
print("unique numbers:",unique(list))