class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result+=num
        if(nums):
            for i in nums:
                self.result += i
        return self

    def subtract(self, num, *nums):
        self.result-=num
        if(nums):
            for i in nums:
                self.result -= i
        return self

        # your code here
        # create an instance:
md = MathDojo()

x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5
