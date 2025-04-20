import math 
def spheresvolume(r):
    V = (4*math.pi*(r**3))/3
    return V

r = float(input("radius:"))
print(spheresvolume(r))
