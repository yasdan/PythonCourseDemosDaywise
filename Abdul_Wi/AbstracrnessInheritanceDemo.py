class shape:
    pass
class rectangle(shape):
    def area(self,lenth,breadth):
         print(f'Area of rectangle ={lenth*breadth}')

class square(shape):
    def area(self,side):
        print(f'Area of Square ={side*side}')

squarearea= square()
squarearea.area(12)
rectanglearea = rectangle()
rectanglearea.area(20,15)

