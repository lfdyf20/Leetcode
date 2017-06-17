import itertools
import numpy as np
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        pass



    def maxSumSubmatrix0(self, matrix, k):
    	res = float('inf')
    	for i, j in itertools.product(range(len(matrix)-1), range(len(matrix[0])-1)):
    		for x, y in itertools.product(range(i+1,len(matrix)), range(j+1,len(matrix[0]))):
    			sumRec = self.compute(i,j,x,y,matrix)
    			print(sumRec)
    			if sumRec <= k and abs(k-sumRec) < abs(k-res):
    				res = sumRec
    	return res

    def compute(self, i, j, x, y, matrix):
    	res = 0
    	# print(matrix[j:y+1][i:x+1])
    	for row in matrix[i:x+1]:
    		res += sum(row[j:y+1])
    	return res

    def online(self, matrix, k):
        import bisect
        maxSum = -9999999
        horizontalSum = [[0 for j in range(0, len(matrix[0]) + 1)] for i in range(0, len(matrix))]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                horizontalSum[i][j] = horizontalSum[i][j - 1] + matrix[i][j]
        print(np.array(horizontalSum))
        for cola in range(0, len(matrix[0])):
            for colb in range(cola, len(matrix[0])):
                bilist, vsum = [0], 0
                for i in range(0, len(matrix)):
                    vsumj = horizontalSum[i][colb] - horizontalSum[i][cola - 1]
                    vsum += vsumj
                    i = bisect.bisect_left(bilist, vsum - k)
                    if i < len(bilist):
                        maxSum = max(maxSum, vsum - bilist[i])
                    bisect.insort(bilist, vsum)
                    print(bilist)
        return maxSum




matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
print(np.array(matrix))
# matrix = [[1, 0, 1]]

k = 2

sl = Solution()
# print( sl.maxSumSubmatrix0( matrix, k ) )
print( sl.online(matrix, k) )


"""
https://www.youtube.com/watch?v=yCQN096CwWM
https://www.quora.com/Given-an-array-of-integers-A-and-an-integer-k-find-a-subarray-that-contains-the-largest-sum-subject-to-a-constraint-that-the-sum-is-less-than-k
You can do this in O(nlog(n))


First thing to note is that sum of subarray (i,j] is just the sum of the first j
 elements less the sum of the first i
 elements. Store these cumulative sums in the array cum. Then the problem reduces to finding  i,j
 such that i<j
 and cum[j]−cum[i]
 is as close to k
 but lower than it.

To solve this, scan from left to right. Put the cum[i]
values that you have encountered till now into a set. When you are processing cum[j]
what you need to retrieve from the set is the smallest number in the set such which is bigger than cum[j]−k
. This lookup can be done in O(logn)
using upper_bound. Hence the overall complexity is O(nlog(n))


Here is a c++ function that does the job, assuming that K>0 and that the empty interval with sum zero is a valid answer. The code can be tweaked easily to take care of more general cases and to return the interval itself.

int best_cumulative_sum(int ar[],int N,int K)
{
    set<int> cumset;
    cumset.insert(0);
    int best=0,cum=0;
    for(int i=0;i<N;i++)
    {
        cum+=ar[i];
        set<int>::iterator sit=cumset.upper_bound(cum-K);
        if(sit!=cumset.end())best=max(best,cum-*sit);
        cumset.insert(cum);
    }
    return best;
}
"""