from collections import defaultdict
class Solution(object):
	def wordsAbbreviation(self, dict):
		"""
		:type dict: List[str]
		:rtype: List[str]
		"""
		abbr2words = defaultdict(set)
		word2abbr = {}

		# group words into abbr
		for word in dict:
			abbr2words[ self.abbrWord(word) ].add( word )

		for abbr, words in abbr2words.items():
			if len(words) > 1:
				for word in words:
					for i in range(2, len(word)):
						prefix = word[:i]
						if self.isUnique(words, prefix):
							word2abbr[ word ] = self.uniqueAbbr(word, prefix)
							break
			else:
				word2abbr[ words.pop() ] = abbr 

		return [ word2abbr[word] for word in dict ]




	def uniqueAbbr(self, word, prefix):
		abbr = prefix + str( len(word) - 1 - len(prefix) ) + word[-1]
		return abbr if len(abbr) < len(word) else word


	def isUnique(self, words, prefix):
		return sum(word.startswith( prefix ) for word in words ) == 1


	def abbrWord(self, word):
		abbr = word[0] + str(len(word)-2) + word[-1]
		return abbr if len(abbr) < len(word) else word




dict = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]

sl = Solution()
print( sl.wordsAbbreviation( dict ) )