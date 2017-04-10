import collections
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.wordDic = collections.defaultdict( set )

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        n = len(word)
        for ind, ch in enumerate(word):
            self.wordDic[ind].add((ch, n-ind))
            self.wordDic[ind].add(('.', n-ind))
            
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        for ind, ch in enumerate(word):
            if self.wordDic[ind] == set():
                return False
            if (ch, n-ind) not in self.wordDic[ind]:
                return False
        return True

class WordDictionary2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        trie = self.trie
        for ch in word:
            trie = trie.setdefault( ch, {} )
        trie['$'] = None

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def find(word, trie):
            if not word:
                return '$' in trie
            char = word[0]
            if char != '.':
                return char in trie and find(word[1:], trie[char])
            return any( find(word[1:], ch) for ch in trie.values() if ch )
        
        return find(word, self.trie)
        
        
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



wordDictionary = WordDictionary()
res = []
wordDictionary.addWord("at")
print( wordDictionary.wordDic )
wordDictionary.addWord("and")
print( wordDictionary.wordDic )
wordDictionary.addWord("an")
print( wordDictionary.wordDic )
wordDictionary.addWord("add")
print( wordDictionary.wordDic )
res.append( wordDictionary.search("a") )
res.append( wordDictionary.search(".at") )
wordDictionary.addWord("bat")
print( wordDictionary.wordDic )
res.append( wordDictionary.search(".at") )
res.append( wordDictionary.search("an.") )
res.append( wordDictionary.search("a.d.") )
res.append( wordDictionary.search("b.") )
res.append( wordDictionary.search("a.d") )
res.append( wordDictionary.search(".") )
print( res )