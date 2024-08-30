class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minVal:
            self.minVal = val

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem == self.minVal:
            if self.stack != []:
                self.minVal = min(self.stack)
            else:
                self.minVal = float('inf')

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()