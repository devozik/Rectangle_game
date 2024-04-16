from random import randint

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
                and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        a = self.upright.x - self.lowleft.x
        b = self.upright.y - self.lowleft.y
        return a * b

rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))
print(f'Rectangle coordinates: {rectangle.lowleft.x}, {rectangle.lowleft.y} and {rectangle.upright.x}, {rectangle.upright.y}')
point = Point(int(input('Guess X:')), int(input('Guess Y: ')))

rec_area = rectangle.area()
guess_area = int(input('Calculate the area of your rectangle: '))
print(f'Your point was inside rectangle: {point.falls_in_rectangle(rectangle)}')
print(f'Your calculations were: {guess_area == rec_area}. Area = {rec_area}')
