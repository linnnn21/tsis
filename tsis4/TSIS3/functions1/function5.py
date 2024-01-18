def permutations(s, permutation=""):
    if len(s) == 0: 
        print(permutation)
    else:
        for i in range(len(s)):
            permutations(s[:i] + s[i+1:], permutation + s[i])  

word = input("Enter a string: ")
print("Permutations:")
permutations(word)
