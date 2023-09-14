class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_circumference(self):
        return 2 * (self.width + self.height)


my_square = Square(5, 10)

print("넓이:", my_square.get_area())
print("둘레:", my_square.get_circumference())
#