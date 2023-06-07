class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if(len(self.min_stack) == 0 and len(self.stack) == 0):
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            self.stack.append(val)
            if(val > self.min_stack[-1]):
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(val)
        

    def pop(self) -> None:
        if(len(self.stack) > 0):
            del self.stack[-1]
            del self.min_stack[-1]
        

    def top(self) -> int:
         if(len(self.stack) > 0):
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()