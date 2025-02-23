def to_ounces(grams):
    ounces =  28.3495231 * grams
    return ounces

grams=float(input("grams:"))
print("ounces=",to_ounces(grams))