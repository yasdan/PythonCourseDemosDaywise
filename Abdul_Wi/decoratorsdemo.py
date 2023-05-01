import  time
import  math
# defining a function to calculate duration of a function execution
def timeScale(func):
    def takeargument(*arg, **more):
        start = time.time() # starting time
        func(*arg,**more)
        close = time.time() # closing time
        print("Execution time for ",func.__name__, close-start)
    return  takeargument

@timeScale   # decorator
def doFactorial(no):
    time.sleep(2)
    print(math.factorial(no))
doFactorial(5)

# Decorator innerfunction returning a value
def doSometaks(func):
    def insideTaks(*arg, **more):
        print("WELCOME")
        somevalue=func(*arg,**more)
        return  somevalue
    return  insideTaks

@doSometaks
def add2Numbers(no1,no2):
    return  no1+no2

print(add2Numbers(20,40))

#Another example for decorator

def showmessage(func):
    def show(*args,**more):
        print("The below result get with code created by ABDUL")
        hi = func(*args, **more)
        return hi
    return  show
@doSometaks
@showmessage    # multiple decorators on a function
@timeScale
def domultiply(no,no1):
    time.sleep(2)
    print(no*no1)

domultiply(23,10)

showmessage(domultiply(10,19)) # Passing argument to decorator

@showmessage
def subtract(no1,no2):
    print(no1-no2)

showmessage(subtract(100,45))# passing argument to decorator
