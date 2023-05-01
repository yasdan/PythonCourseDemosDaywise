def add(num1,num2):
  return num1+num2

def subtract(num1,num2):
  return num1-num2

def multiply(num1,num2):
  return num1*num2

def divide(num1,num2):
  return num1/num2

operations= {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

n1= int(input("Enter 1st number"))
for symbol in operations:
  print(symbol)

operationSymbol= input("Pick a symbol from the above lines")

n2= int(input("Enter 2nd number"))
calculateFunction=operations[operationSymbol]
answer=calculateFunction(n1,n2)
print(f"{n1} {operationSymbol} {n2}= {answer}")
