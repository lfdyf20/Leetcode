from collections import Counter, defaultdict, deque
from itertools import combinations
import numpy as np
import time
import sys
import random
from math import sqrt



a = {1:2,5:6}
print( a.setdefault(3,2) )
print( a.get(4,0) )
print(a)


matrix = [
	[1,0,1,0,0],
	[1,0,1,1,1],
	[1,1,1,1,1],
	[1,0,0,1,0]
]

print( matrix[0] )
print( list(zip(*matrix))[0] )