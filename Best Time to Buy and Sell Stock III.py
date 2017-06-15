import numpy as np
class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		""" 

		if len(prices) < 2:
			return 0
		k = 2
		dp = [0 for _ in range(len(prices))]
		for i in range(1, k+1):
			temp_max = dp[0] - prices[0]
			for j in range(1, len(prices)):
				temp = temp_max
				temp_max = max( temp_max, dp[j]-prices[j] )
				dp[j] = max( dp[j-1], prices[j]+temp )
		return dp[-1]

	def mySolution(self, prices):
		if len(prices) < 2:
			return 0
		K = 2
		dp = [[0]*len(prices) for _ in range(K+1)]
		for k in range(1, K+1):
			temp = dp[k-1][0] - prices[0]
			for i in range(1, len(prices)):
				print(i, prices[i])
				print(temp)
				dp[k][i] = max(dp[k][i-1], prices[i]+temp)
				temp = max(temp, dp[k-1][i]-prices[i] )
				print(np.array(dp))
				
		print(np.array(dp))
		return dp[-1][-1]


prices = [1,3,1,4,5,9,2,6]
prices = [3,3,5,0,0,3,1,4]

sl = Solution()
print( sl.maxProfit( prices ) )
print( sl.mySolution(prices) )



"""
class Solution {
public:
	int maxProfit(vector<int> &prices) {
		// f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions. 
		// f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
		//          = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
		// f[0, ii] = 0; 0 times transation makes 0 profit
		// f[k, 0] = 0; if there is only one price data point you can't make any money no matter how many times you can trade
		if (prices.size() <= 1) return 0;
		else {
			int K = 2; // number of max transation allowed
			int maxProf = 0;
			vector<vector<int>> f(K+1, vector<int>(prices.size(), 0));
			for (int kk = 1; kk <= K; kk++) {
				int tmpMax = f[kk-1][0] - prices[0];
				for (int ii = 1; ii < prices.size(); ii++) {
					f[kk][ii] = max(f[kk][ii-1], prices[ii] + tmpMax);
					tmpMax = max(tmpMax, f[kk-1][ii] - prices[ii]);
					maxProf = max(f[kk][ii], maxProf);
				}
			}
			return maxProf;
		}
	}
};
"""