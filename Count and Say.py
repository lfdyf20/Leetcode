class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """ 
        s = "1"
        for _ in range(1, n):
            temp, curr, count = '', s[0], 0
            for ch in s:
                if ch == curr:
                    count += 1
                else:
                    temp += str(count) + curr
                    curr = ch
                    count = 1
            temp += str(count) + curr
            s = temp
        return s



    #     seq = "1"
    #     if n == 1:
    #     	return seq
        
    #     while n > 1:
    #     	seq = self.generateSeq(seq)
    #     	n -= 1
    #     return seq



    # def generateSeq(self, seq):
    # 	"""
    # 	Arguments:
    # 		seq {str}
    # 		rtype: str
    # 	"""
    # 	res = ""
    # 	last = ""
    # 	number = 0
    # 	for i in xrange(len(seq)):
    # 		if seq[i] == last:
    # 			number = number + 1
    # 		else:
    # 			if i==0:
    # 				res = res + last
    # 			else:
    # 				res = res + str(number) + last
    # 			number = 1
    # 			last = seq[i]
    # 	#print type(res), type(last * number),last, number
    # 	res = res + str(number) + last
    # 	return res






n = 3
sample =Solution()
print(sample.countAndSay(n))