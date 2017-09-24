class Solution(object):
	# REVIEW: the algo
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        index = {num: i for i, num in enumerate([None] + org)}
        print(index)
        pairs = set(zip([None] + org, org))
        print(pairs)
        for seq in seqs:
        	for a,b in zip([None] + seq, seq):
        		if index[a] >= index.get(b, 0):
        			return False
        		pairs.discard((a,b))
        return not pairs


org, seqs = [1,2,3], [[1,2],[1,3],[2,3]]

sl = Solution()
print( sl.sequenceReconstruction( org, seqs ) )

# https://discuss.leetcode.com/topic/65633/very-short-solution-with-explanation