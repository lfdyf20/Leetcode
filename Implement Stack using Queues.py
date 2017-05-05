from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque([])
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q = self.queue
        q.append(x)
        for _ in range(len(q)-1):
            q.append( q.popleft() )
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.popleft()

        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0] if not self.empty() else None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self.queue)
        


# Your MyStack object will be instantiated and called as such:
x = 2
obj = MyStack()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

print(param_2, param_3, param_4)