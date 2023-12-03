class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def display(self):
        print(f'{self.name} has an area of {self.area} and perimeter of {self.perimeter}')

class Square(Shape):
    def __init__(self, side):
        super().__init__('Square')
        self.side = side
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()

    def compute_area(self):
        return self.side ** 2
    
    def compute_perimeter(self):
        return 4 * self.side

s = Square(4)
s.display()