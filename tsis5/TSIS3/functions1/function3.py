def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits = numheads - chickens
        if chickens*2+rabbits*4 == numlegs:
            return chickens,rabbits
        
numheads = 35
numlegs = 94

chickens, rabbits = solve(numheads, numlegs)
print("chickens:",chickens,"and rabbits:", rabbits,"rabbits")