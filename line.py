import math


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def rise(self):
        return self.p2[1] - self.p1[1]

    def run(self):
        return self.p2[0] - self.p1[0]

    def slope(self):
        return self.rise() / self.run()

    def y_intercept(self):
        return self.p1[1] - (self.p1[0] * self.slope())

    def isvertical(self):
        try:
            self.slope()
            return False
        except ZeroDivisionError:
            return True

    def ishorizontal(self):
        return self.p1[1] == self.p2[1]

    def perpendiculardistancehorizontal(self, point):
        return abs(self.p1[1] - point[1])

    def perpendiculardistancevertical(self, point):
        return abs(self.p1[0] - point[0])

    def perpendiculardistancehasslope(self, point):
        return abs(((self.slope() * point[0]) - point[1] + self.y_intercept()) / math.sqrt(
            (math.pow(self.slope(), 2))) + 1)

    def perpendiculardistance(self, point):
        if self.isvertical():
            return self.perpendiculardistancevertical(point)
        elif self.ishorizontal():
            return self.perpendiculardistancehorizontal(point)
        else:
            return self.perpendiculardistancehasslope(point)
