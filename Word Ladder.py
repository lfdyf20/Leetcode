import time
from collections import deque
from collections import defaultdict
from itertools import combinations
from tryFunc import timer


class Solution(object):
    @timer
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

    @timer
    def mySolution(self, beginWord, endWord, wordList):
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

        visited = set()
        res = 1
        stack = deque([ beginWord, '$1' ])
        # print(rec)
        while stack:
            # print(stack)
            word = deque.popleft(stack)
            if word[0] == '$':
                res += 1
                stack.append('$'+str(res))
                continue
            visited.add( word )
            for nextWord in rec[word]:
                rec[nextWord].remove(word)
                if nextWord == endWord:
                    # print("find it")
                    return res+1
                if nextWord not in visited:
                    visited.add(nextWord)
                    stack.append(nextWord)
            rec[word] = set()
        return 0






beginWord = "hit"
endWord = "coa"
wordList = ["hot","dot","dog","lot","log", "tbc", "cig", "cit", "cia", "hta", "hoa"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "hit"
endWord = "hot"
wordList = ["hot","dot","dog","lot","log","cog"]

sl = Solution()


print( sl.ladderLength( beginWord, endWord, wordList ) )
print( sl.mySolution(beginWord, endWord, wordList) )