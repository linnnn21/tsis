def palindrom(word):
    if word==word[::-1]:
        print("Yes")
    else:
        print("No")

word = input("word: ")
palindrom(word)