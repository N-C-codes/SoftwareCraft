"""
To implement: String methods using TDD:

1. to_upper(): converts a string to upper case
2. to_lower(): converts a string to lower case
3. reverse(): reverses a string
"""

class String:
    
    def __init__(self, value):
        self.value = value
    
    def to_lower(self):
        return self.value.lower()
    
    def to_upper(self):
        return self.value.upper()
    
    def reverse(self):
        return self.value[::-1]