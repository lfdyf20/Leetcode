import time
from collections import deque
from collections import defaultdict
from itertools import combinations
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        def constructDic( words ):
            dic = {}
            for word in words:
                for i in range( len(word) ):
                    s = word[:i] + '_' + word[i+1:]
                    dic[ s ] = dic.get( s, [] ) + [word]
            return dic


        def bfs( begin, end, dic ):
            queue = deque( [(begin, 1)] )
            visited = set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add( word )
                    if word == end:
                        return steps
                    for i in range( len(word) ):
                        s = word[:i] + '_' + word[i+1:]
                        nextWords = dic.get(s, [])
                        for nextWord in nextWords:
                            if nextWord not in visited:
                                queue.append( (nextWord, steps+1) )
            return 0



        d = constructDic( set(wordList) | set([beginWord, endWord])) 
        # print(d)
        return bfs(beginWord, endWord, d)
        

    def ll(self, beginWord, endWord, wordList):
        def check(word1, word2):
            count = 0
            for i, j in zip(word1, word2):
                if i != j:
                    count += 1
            if count == 1:
                return True
            else:
                return False

        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            wordList.append( endWord )
        rec = defaultdict( set )
        for i, j in combinations(wordList, 2):
            if check( i, j ) == True:
                rec[ i ].add(j)
                rec[ j ].add(i)
        # print(rec)

        count = 0

        visited = set()
        leaves = set([ beginWord ])

        while count < 10:
            count += 1
            newleaves = set()
            for word in leaves:
                # print( "curr word is : ", word )
                visited.add( word )

                if endWord in visited:
                    return count
                if len(visited) == len( wordList ):
                    return 0

                newleaves = newleaves | rec[ word ]
            if leaves == newleaves:
                return 0
            leaves = newleaves.copy()
            # print(leaves)
            

        # rec = defaultdict(set)
        # for word in wordList:







beginWord = "hit"
endWord = "coa"
wordList = ["hot","dot","dog","lot","log", "tbc", "cig", "cit", "cia", "hta", "hoa"]

sl = Solution()

st = time.time()
print( sl.ladderLength( beginWord, endWord, wordList ) )
print( time.time() - st )

# st = time.time()
# print( sl.ll( beginWord, endWord, wordList ) )
# print( time.time() - st )