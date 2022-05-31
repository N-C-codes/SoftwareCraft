"""
Coding an example in Python that uses the Bridge Design Pattern.
"""

class Square:
    
    def area(self, length, width=None):
        return length * length
    
    def perimeter(self, length, width=None):
        return 4 * length
    
class Rectangle:
    
    def area(self, length, width):
        return length * width
    
    def perimeter(self, length, width):
        return 2 * (length + width)
    
class BridgeClass:
    def __init__(self, shape, length, width=None):
        
        self._shape = shape
        self._length = length
        self._width = width
    
    def area(self):
        return self._shape.area(self._length, self._width)

    def perimeter(self):
        return self._shape.perimeter(self._length, self._width)
    
sq = BridgeClass(Square(), 5)
rec = BridgeClass(Rectangle(), 4, 5)

print(sq.area()) # Should be 25
print(rec.area()) # Should be 20

print(sq.perimeter()) # Should be 20
print(rec.perimeter()) # Should be 18