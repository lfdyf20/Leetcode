from collections import defaultdict

class TrieNode(object):
	"""
	A node for Trie
	"""
	def __init__(self):
		self.nodes = defaultdict( TrieNode )
		self.isWord = False

class Trie(object):
	"""
	A Class for Trie
	Methods:
	- insert(word)
	- search(word)
	- startsWith(prefix)
	"""
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		curr = self.root
		for letter in word:
			curr = curr.nodes[ letter ]
		curr.isWord = True

	def search(self, word):
		curr = self.root
		for letter in word:
			if letter not in curr.nodes:
				return False
			curr = curr.nodes[ letter ]
		return curr.isWord

	def startsWith(self, prefix):
		curr = self.root
		for letter in prefix:
			if letter not in curr.nodes:
				return False
			curr = curr.nodes[ letter ]
		return True