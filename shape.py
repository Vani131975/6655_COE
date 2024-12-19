class Shape:

  def __init__(self):
    pass

  def area(self):
    print("the area of shape is: 0")


class Square(Shape):

  def __init__(self, length):
    super().__init__()
    self.length = length

  def area(self):
    self.area = self.length**2
    print("The area of the square is: ", self.area)


shape = Shape()
shape.area()
square = Square(4)
square.area()
