def timer(func):
    def wrapper(*args, **ks):
        import time
        start = time.time()
        res = func(*args, **ks)
        print(time.time()-start)
        return res
    return wrapper


class Solution(object):
    @timer
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

    @timer
    def mySolution(self, coins, amount):
        res = [0]+[float('inf')]*amount
        for i in range(1,len(res)):
            res[i] = min([res[i-val] for val in coins if i-val>=0] or [float('inf')])+1
        # print(res)
        return res[-1] if res[-1] != float('inf') else -1




coins = [3,7,405,436]
amount = 8839

# coins = [1,2,5]
# amount = 11

sl = Solution()
print( sl.coinChange( coins, amount ) )
print( sl.mySolution(coins, amount) )