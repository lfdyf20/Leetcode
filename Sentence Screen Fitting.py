class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        """
        need more improvement about time complexicty!
        """
        s = 0
        n = len(sentence)
        for i in range(rows):
        	count = 0

        	if s != 0 and s%n == 0:
        		return int((rows*1.0/i * s) / len(sentence))
        	while True:
        		print( s, n, s%n )
        		if count + len(sentence[ s % n ]) > cols:
        			break
        		count += len(sentence[ s % n ])
        		s += 1
        		if count == cols:
        			break
        		else:
        			count += 1
        return s // len(sentence)


    def online(self, sentence, rows, cols):
    	s = ' '. join(sentence)
    	ind = 0
    	for i in range(rows):
    		ind += cols - 1
    		if s[ ind % len(s) ] == ' ':
    			ind += 1
    		elif s[ (ind+1) % len(s) ] == ' ':
    			ind += 2
    		else:
    			while ind > 0 and s[(ind-1)%len(s)] != ' ':
    				ind -= 1
    	return ind // len(s)


        	 
        



rows = 4
cols = 5
sentence = ["I", "had", "apple", "pie"]

rows = 3
cols = 6
sentence = ["a", "bcd", "e"]

rows = 2
cols = 8
sentence = ["hello", "world"]

sentence = ["try","to","be","better"]
rows = 10000
cols = 9001

sentence = ["f","p","a"]
rows = 8
cols = 7

sl = Solution()
print( sl.wordsTyping( sentence, rows, cols ) )