class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        
        






n = 1000000
primes = [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]
sl = Solution()
# print( sl.nthSuperUglyNumber( n, primes ) )

# print( sl.isSuperUglyNum( 13**5*2*19, primes ) )





    # def nthSuperUglyNumber(self, n, primes):
    #     """
    #     :type n: int
    #     :type primes: List[int]
    #     :rtype: int
    #     """
    #     k, number = 0, 0 
    #     while k < n:
    #     	number += 1
    #     	if self.isSuperUglyNum( number, primes):
    #     		if number > primes[-1]:
    #     			primes.append( number )
    #     		k += 1      		
    #     return number
        		

    # def isSuperUglyNum(self, number, primes):
    # 	for i in primes:
    # 		while number % i == 0:
    # 			number = number / i
    # 			if number == 1:
    # 				return True
    # 	return False



class Solution2(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        nums=[1]*len(primes)
        idx=[0]*len(primes)
        best=[1]
        cur=1
        for i in range(n-1):
            for j in range(len(idx)):
                if nums[j]==cur:
                	print( "i:",i, "   j:",j )
                	nums[j]=best[idx[j]]*primes[j]
                	idx[j]+=1
                	print("nums[j]=", nums[j])
                	print("idx[j]=", idx[j])
            cur=min(nums)
            best.append(cur)
        return best[-1]




n = 10
primes = [2, 7, 13, 19]
sl = Solution2()
print( sl.nthSuperUglyNumber( n, primes ) )