import time
import math

def square_root(number, delay):
    time.sleep(delay / 1000)  
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay} milliseconds is {result}")

num, delay = map(int, input("Enter a number and delay in milliseconds: ").split())
square_root(num, delay)
