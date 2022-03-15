
class square:

    def __init__(self,side):
        self.side = side

    def __add__(squareone,square2):
        return((4*squareone.side)+(4*square2.side))


squareone = square(5)
square2 =square(10)

print("sum of the both sides of the square = " , squareone + square2).