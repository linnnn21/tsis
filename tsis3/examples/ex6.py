def myfunction():
  pass

#if you for some reason have a function definition with no content, the pass statement to avoid getting an error

def my_function(a, b, /, c):   #/ -al arguments before it must be passed by position only
    print(a, b, c)

my_function(1, 2, 3)       # Works (all positional)
my_function(1, 2, c=3)     # Works (c passed as keyword)
my_function(a=1, b=2, c=3) # Error: a and b must be positional-only
