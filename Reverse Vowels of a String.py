class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        vowelsList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sList = list( s )
        i, j = 0, len(sList)-1
        while i<j:
        	if sList[i] in vowelsList and sList[j] in vowelsList:
        		# print( 'now the vowels to swap: '+ repr(sList[i]) + repr(sList[j]) , i, j)
        		sList[i], sList[j] = sList[j], sList[i]
        		i += 1
        		j -= 1
        	elif sList[i] not in vowelsList and sList[j] not in vowelsList:
        		# print("sList[i] and sList[j]:",i, j, sList[i],sList[j], "not in vowelsList")
        		i += 1
        		j -= 1
        	elif sList[i] not in vowelsList:
        		# print( 'sList[i]',i,sList[i],'not in vowelsList' )
        		i += 1
        	elif sList[j] not in vowelsList:
        		# print( 'sList[j]',j,sList[j],'not in vowelsList' )
        		j -= 1
        return ''.join(sList)


s = "hello"
sl = Solution()
print( sl.reverseVowels( s ) )
# print( len(s)-1 )
# print( s[4] )
# sList = list( s )
# vowelsList = ['a', 'e', 'i', 'o', 'u']
# print( ('e' and 'l') in vowelsList )
# print( 'l' in vowelsList )