def function(food):
    for x in food:
        print(x)

fruits = ["apple" , "21" , "qwe"] # it will be treated as the same data type inside the function
function(fruits)


def my_function(a, b, *, c, d):
    print(a, b, c, d)

my_function(1, 2, c=3, d=4)  # Works
my_function(1, 2, 3, 4)      # Error: c and d must be keyword arguments 