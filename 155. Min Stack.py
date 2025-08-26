class MinStack(object):

    def __init__(self):
        self.stack = []        # основной стек
        self.min_stack = []    # стек для хранения минимальных значений
       
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            raise Exception("Stack is empty")
        
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise Exception("Stack is empty")
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_stack:
            raise Exception("Stack is empty")
        return self.min_stack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
