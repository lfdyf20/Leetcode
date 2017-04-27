class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        sef.dic = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if timestamp >= self.dic.get( message, 0 ):
            self.dic[message] = timestamp+10
            return True
        return False


# # Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)