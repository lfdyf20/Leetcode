U_class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack ==[]:
            return None
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """ 
        return len(set(self.stack))



sample = MinStack()
print sample.stack

sample.push(1)
print sample.stack

print sample.pop()

print sample.top()

print sample.getMin()
