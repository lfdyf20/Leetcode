# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
import random


# random.seed(3)
def pick(n):
	trueVal = random.randint( 1, n )
	return trueVal

def guess(x):
	return 1 if trueVal>x else [-1,0][trueVal == x]
	

class Solution(object):
	def guessNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		i = 0
		minVal, maxVal = 0, n
		while True:
			i += 1
			# if i > 10:
			# 	return False
			t = round( (minVal + maxVal)/2 )
			# print(minVal,'\t', maxVal,'\t', t)
			evl = guess( t )
			if evl == 0:
				# print("step:",i)
				return t
			elif evl == 1:
				minVal = t
			elif evl == -1:
				maxVal = t
			else:
				print('error')
				return False

	def mySolution(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		l, h = 1, n
		mid = (l+h)//2
		r = guess( mid )
		while r != 0 and l<h:
			if r == 1:
				l = mid+1
			elif r == -1:
				h = mid-1
			mid = (l+h)//2
			r = guess( mid )
		return mid
				
	   

n = 10
trueVal = pick( n )
print(trueVal)

sl = Solution()
print( sl.guessNumber(n) )
print( sl.mySolution(n) )

