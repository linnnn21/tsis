def count_case_letters(text):
    upper_count = sum(1 for i in text if i.isupper())  
    lower_count = sum(1 for i in text if i.islower()) 

    print("The number of uppercase letters:", upper_count) 
    print("The number of lowercase letters:", lower_count)  

text = input("Enter a string: ")
count_case_letters(text)
