import math

class Operation:
    def execute(self, a, b=None):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)
