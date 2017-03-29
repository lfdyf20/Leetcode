from random import randint
import numpy as np

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Solution(object):
	def canConnect(self, A, B, P, Q):
		if A.x == B.x:
			abSet = set( [ (A.x, i) for i in range(min(A.y, B.y), max(A.y,B.y)+1) ] )
		else:
			abset = set( [ (i, A.y) for i in range(min(A.x, B.x), max(A.x,B.x)+1) ] )
		if P.x == Q.x:
			pqSet = set( [ (P.x, i) for i in range(min(P.y, Q.y), max(P.y,Q.y)+1) ] )
		else:
			pqSet = set( [ (i, P.y) for i in range(min(P.x, Q.x), max(P.x,Q.x)+1) ] )
		return len( abset & pqSet) > 0


	def mysolution2(self, A, B, C, D):
		if A.y == B.y:
			if P.y == Q.y:
				if A.y == P.y:
					if max(P.x,Q.x)<min(A.x,B.x) or min(P.x,Q.x)<max(A.x,B.x):
						return True
					else:	return False
				else:	return True
			else:
				if P.x>=min(A.x,B.x) and P.x<=max(A.x,B.x) and A.y>=min(P.y,Q.y) and A.y<=max(P.x,Q.x):
					return False
				else:
					return True
		else:
			if P.x == Q.x:
				if A.x == P.x:
					if max(P.y,Q.y)<min(A.y,B.y) or min(P.y,Q.y)<max(A.y,B.y):
						return True
					else:	return False
				else:	return True
			else:
				if P.y>=min(A.y,B.y) and P.y<=max(A.y,B.y) and A.x>=min(P.x,Q.x) and A.x<=max(P.y,Q.y):
					return False
				else:
					return True









n = 5

A = Point( 0, 1 )
B = Point( 4, 1 )
P = Point( 1, 0 )
Q = Point( 1, 5 )

A = Point( 2, 1 )
B = Point( 3, 1 )
P = Point( 0, 1 )
Q = Point( 5, 1 )

sl = Solution()
print( sl.canConnect(A, B, P, Q) )
print( sl.canConnect(A, B, P, Q) )






