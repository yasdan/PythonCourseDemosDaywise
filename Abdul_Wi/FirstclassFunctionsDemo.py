def printinUpper(data):
    return data.upper()

pt= printinUpper("hello! welcome!") # function assigning to variable
print(pt)

hl = printinUpper     # function treated as object
print(hl("wish you won this game"))

def printinLower(data):
    return  data.lower()

# function creating & can be passed as argument
def funargument(myfun):
    hifun= myfun("A function can be Created & Passed as Argument")
    print(hifun)

funargument(printinUpper)  # function passed as argument

funargument(printinLower)

# A function can return another functon
def jumbotrac(text):
    def smalltrac(mytext):
        return  text+" "+mytext
    return smalltrac

jt=jumbotrac("Welcome")
print(jt("Python programer"))

# Closures in nested functions

def firstName(fname):
   def fullName(lname):
       print(fname+" "+lname)
    # returning function
   return fullName

myname = firstName ("Sunil")
myname("Kumar")

