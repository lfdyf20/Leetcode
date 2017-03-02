class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for string in strings:
        	first = string[0]
        	key = []
        	for letter in string[1:]:
        		diff = ord(letter)-ord(first)
        		diff = diff if diff>0 else 26+diff 
        		key.append( diff )
        	key = tuple(key)
        	if key in dic:
        		dic[ key ].append( string )
        	else:
        		dic[ key ] = [ string ]
        return list(dic.values())





strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

sl = Solution()
print( sl.groupStrings( strings ) )