from collections import defaultdict

class TrieNode(object):

    def __init__(self):
        self.nodes = defaultdict( TrieNode )
        self.isWord = False



class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for letter in word:
            curr = curr.nodes[ letter ]
        curr.isWord = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for letter in word:
            if letter not in curr.nodes:
                return False
            curr = curr.nodes[ letter ]
        return curr.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for letter in word:
            if letter not in curr.nodes:
                return False
            curr = curr.nodes[ letter ]
        return True
        


# Your Trie object will be instantiated and called as such:
words = ["hello", "world", "word", "he"]
obj = Trie()
for word in words:
    obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)