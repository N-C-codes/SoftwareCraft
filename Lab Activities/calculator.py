class Calculator:
    
    def __init__(self):
        pass
    
    def parse(self, numbers):
        
        # Input numbers should be a string of two values separated by a comma:
        self.numbers = numbers
        if type(self.numbers[0]) is not str:
            raise TypeError("Please enter a string!")
        else:
            self.nums = self.numbers[0].split(",")
            self.first_num = int(self.nums[0])
            self.second_num = int(self.nums[1])
            
            return (self.first_num, self.second_num)
    
    def add(self, *numbers):
        nums = self.parse(numbers)
        num_1 = nums[0]
        num_2 = nums[1]
        
        return num_1 + num_2
    
    def subtract(self, *numbers):
        nums = self.parse(numbers)
        num_1 = nums[0]
        num_2 = nums[1]
        
        return num_1 - num_2
    
    def multiply(self, *numbers):
        nums = self.parse(numbers)
        num_1 = nums[0]
        num_2 = nums[1]
        
        return num_1 * num_2
    
    def divide(self, *numbers):
        nums = self.parse(numbers)
        num_1 = nums[0]
        num_2 = nums[1]
        
        if num_2 != 0:
            return num_1 / num_2
        else:
            raise ZeroDivisionError("You cannot divide by zero!")
        