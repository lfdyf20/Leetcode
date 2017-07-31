from collections import defaultdict

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        _trie = lambda: defaultdict(_trie)

        trie = _trie()
        END = True

        for word in dict:
        	cur = trie
        	for letter in word:
        		cur = cur[letter]
        	cur[END] = word

        def replace(word):
        	cur = trie
        	for letter in word:
        		if letter not in cur:
        			break
        		cur = cur[letter]
        		if END in cur:
        			return cur[END]
        	return word

        return " ".join(map(replace, sentence.split()))



dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

sl = Solution()
print( sl.replaceWords( dict, sentence ) )