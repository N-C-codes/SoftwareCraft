class Calculator:
    
    def __init__(self):
        pass
    
    def parse(self, numbers):
        
        # Input numbers should be a string of two values separated by a comma:
        self.numbers = numbers
        if type(self.numbers[0]) is not str:
            raise TypeError("Please enter a string!")
        elif self.numbers[0] == "":
            return (0,0, "empty")
        else:
            self.nums = self.numbers[0].split(",")
            if len(self.nums) == 1:
                return (int(self.nums[0]),)
            else:
                self.first_num = int(self.nums[0])
                self.second_num = int(self.nums[1])
                
                return (self.first_num, self.second_num)
    
    def add(self, *numbers):
        nums = self.parse(numbers)
        if len(nums) == 1:
            return nums[0]
        else:
            return nums[0] + nums[1]
    
    def subtract(self, *numbers):
        nums = self.parse(numbers)
        if len(nums) == 1:
            return nums[0]
        else:
            return nums[0] - nums[1]
    
    def multiply(self, *numbers):
        nums = self.parse(numbers)
        if len(nums) == 1:
            return nums[0]
        else:
            return nums[0] * nums[1]
    
    def divide(self, *numbers):
        nums = self.parse(numbers)
        if len(nums) == 1:
            return nums[0]
        else:
            num_1 = nums[0]
            num_2 = nums[1]
            
            if num_2 != 0:
                return num_1 / num_2
            elif len(nums) > 2:
                return 0
            else:
                raise ZeroDivisionError("You cannot divide by zero!")
        