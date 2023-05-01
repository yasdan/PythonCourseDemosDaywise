
# def squareit(no):
#     return  no*no

#mynumbers =[12,3,5,17]

#squares = map(squareit,mynumbers)
#print(list(squares))

# Generator example
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse("lips"):
    print(char)

# Generator Expressions
sm=sum(i*i for i in range(5))
print(sm)

cubes = (i**3 for i in range(10))
print(cubes)
print(list(cubes))

xvector =[10,20,40]
yvector=[6,4,2]
total=sum(x*y for x,y in zip(xvector,yvector))
print(total)
