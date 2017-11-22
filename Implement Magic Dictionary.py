from collections import Counter
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.words = []
        self.dics = set( dict )
        self.neighbor =  Counter(cand for word in words
            for cand in self.candidate(word))
       

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """ 
        return any(self.neighbor[cand] > 1 or 
                   self.neighbor[cand] == 1 and word not in self.words
                   for cand )



    def candidate(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]