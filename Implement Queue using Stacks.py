class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack_in.append( x )
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out.pop()

        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack_in == self.stack_out == []
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2, param_3, param_4)