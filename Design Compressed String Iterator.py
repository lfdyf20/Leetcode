import re
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.chars = re.findall(r'\D', compressedString)[::-1]
        self.counts = re.findall(r'\d+', compressedString)[::-1]
        self.count = 0
        self.char = ''
        
    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return ' '
        if self.count:
            self.count -= 1
            return self.char
        self.count = int(self.counts.pop())
        self.char = self.chars.pop()
        self.count -= 1
        return self.char
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.count or self.counts:
            return True
        return False


# Your StringIterator object will be instantiated and called as such:
iterator = StringIterator("L1e2t1C1o1d1e1");

print(iterator.next()); # return 'L'
print(iterator.next()); # return 'e'
print(iterator.next()); # return 'e'
print(iterator.next()); # return 't'
print(iterator.next()); # return 'C'
print(iterator.next()); # return 'o'
print(iterator.next()); # return 'd'
print(iterator.hasNext()); # return true
print(iterator.next()); # return 'e'
print(iterator.hasNext()); # return false
print(iterator.next()); # return ' '