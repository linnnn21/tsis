def palindrome(text):
    text2 = "".join(reversed(text))
    if text.lower() == text2.lower():
        print("It is palindrome")
    else:
        print("No, it's not palindrome")

text = input("Enter some string: ")
palindrome(text)
