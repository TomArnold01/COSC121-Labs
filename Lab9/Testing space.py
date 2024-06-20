class Point:
    """ a point with an initialiser and a __str__ method"""
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __str___(self):
        """Method to retrun a string rep of self"""
        return "(x: {0}, y: {1}) ".format(self.x, self.y)

    def __repr__(self):
        """ reutrns the represrntaion of self"""
        return "Point:({}, {})".format(self.x, self.y)

point = Point(10, 20)
print(point)
print("Point = " + str(point))