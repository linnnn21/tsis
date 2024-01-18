'''
*args = many values without names.
**kwargs = many values with names. '''
def function(**kid):
    print("His last name is" + kid["lname"])

function(fname = "Tobias" , lname = "Refsnes")