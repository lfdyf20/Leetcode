class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        Max = float('inf')
        record = [0] + [Max] * amount
        for i in range(1, amount+1):
        	record[i] = min( [ record[i-c] if i-c>=0 else Max for c in coins ] ) + 1
        return [ record[amount], -1 ][ record[amount] == Max ]


    #This is slow 
    #     coins.sort(reverse = True)
    #     res = self.countLen(coins, amount)
    #     if res == float('inf'):
    #     	return -1
    #     return res
       
    # def countLen(self, coins, amount):
    # 	if amount == 0:
    # 		return 0
    # 	if amount < 0 or coins==[]:
    # 		return float("inf")
    # 	return min(self.countLen(coins, amount-coins[0])+1, 
    # 				self.countLen(coins[1:],amount-coins[0])+1, 
    # 				self.countLen(coins[1:],amount))





coins = [3,7,405,436]
amount = 8839

sl = Solution()
print( sl.coinChange( coins, amount ) )