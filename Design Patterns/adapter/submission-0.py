class SquareHole:
    def __init__(self, length):
        self.length = length

    def canFit(self, square):
        return square.getSideLength() <= self.length


class Square:
    def __init__(self, sideLength):
        self.sideLength = sideLength

    def getSideLength(self):
        return self.sideLength


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius


class CircleToSquareAdapter(Square):
    def __init__(self, circle):
        self.circle = circle

    def getSideLength(self):
        return self.circle.getRadius() * 2