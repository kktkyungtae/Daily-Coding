class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

class Circle:
    pi = 3.14

    def __init__(self,center,r):
        self.center = center
        self.r = r

    def get_area(self):
        return round(Circle.pi * self.r * self.r,2)

    def get_perimeter(self):
        return  Circle.pi * self.r * 2

    def get_center(self):
        Center = ()
        Center = (self.center.x,self.center.y)
        return Center

    def print(self):
        print(f'Circle: {(self.center.x,self.center.y)}, r: {self.r}')

p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()