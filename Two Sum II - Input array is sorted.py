class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # numberSet = list( set( numbers ) )
        # numberSet.sort()
        # for i in range( len(numberSet) ):
        # 	val = target - numberSet[i]
        # 	if val == numberSet[i]:
        # 		loc = numbers.index( val )
        # 		return [loc+1, loc+2]
        # 	elif val in numberSet:
        # 		loc1 = numbers.index( numberSet[i] )
        # 		loc2 = numbers.index( val )
        # 		return [loc1+1, loc2+1] 
        # 	else:
        # 		print( 'else: i', numberSet[i] )
        # 		pass
        # return False
        i, j = 0, len(numbers)-1
        while i<j:
        	val = numbers[i]+numbers[j]
        	if  val == target:
        		return [i+1, j+1]
        	elif val < target:
        		i += 1
        	else:
        		j -= 1




numbers = [-3,3,4,90]
target = 0

sl = Solution()
print( sl.twoSum( numbers, target ) )