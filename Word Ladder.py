from collections import deque
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
        return bfs(beginWord, endWord, d)
        


     

    #     dic = {}
    #     for word in wordList:
    #     	if word[0] in dic:
    #     		if word[-1] in dic[word[0]]:
    #     			continue
    #     		else:
    #     			dic[word[0]].append( word[0] )
    #     	else:
    #     		dic[word[0]] = [word[-1]]
        
    #     st = beginWord[0]
    #     ed = endWord[0]
    #     minV = self.travel( st, ed, dic )
    #     print(minV)

    # def travel(self, st, ed, dic):
    # 	print(st, ed)
    # 	print(dic)
    # 	if ed in dic[st]:
    # 		return 1
    # 	minV = 1000
    # 	for i in dic[st]:
    # 		minV = min(self.travel( i, ed, dic)+1, minV)
    # 	return minV





beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log", "tbc"]

sl = Solution()
print( sl.ladderLength( beginWord, endWord, wordList ) )