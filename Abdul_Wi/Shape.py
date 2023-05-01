class shape:
    def area(self):   # abstract method
        pass

class Rectangle(shape):       #over riden method
    def area(self,lenth, breadth):
        rectarea= lenth*breadth
        return  rectarea

rect = Rectangle()
res=rect.area(13,23)
print("Rectangle area= ",res)

class triangle(shape):
    def area(self,breadth, height):
        trianglearea = 0.5*breadth*height
        return  trianglearea

trg= triangle()
res=trg.area(12,8)
print(f'Triangle area = {res}')
