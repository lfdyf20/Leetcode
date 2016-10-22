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