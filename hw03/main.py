import math
class Rectangle():
    def __init__(self,width,height):
        self.square=width*height
    
class Square(Rectangle):
    def __init__(self,sideLine):
        self.square=sideLine**2

class Ellipse(Rectangle):
    def __init__(self,width,height):
        self.square=math.pi*width*height

class Circle(Ellipse):
    def __init__(self,radius):
        self.square=math.pi*radius**2

def compute_area(list):
    sum=0
    for i in list:
        sum+=i.square
        #print(i.square)
    return sum

shapes = [Ellipse(10,20), Square(15), Circle(5), Rectangle(20,15), Circle(5), Square(15), Ellipse(10,20)]
total_area=compute_area(shapes)
print('%f'%total_area)
