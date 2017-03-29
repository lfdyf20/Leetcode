from collections import Counter, defaultdict, deque
from itertools import combinations
import numpy as np
import time
import sys
import random
from math import sqrt



# a = "/qihoo/app/a/b/c/d/new.c"
# b = "/qihoo/app/1/2/test.c"

# aa = a.split('/')
# bb = b.split('/')
# res = ''
# tail = ''
# for i in range(len(a)):
# 	if aa[i]==bb[i]:
# 		continue
# 	print(i)
# 	res += '../'*(len(aa)-i-1) + '/'.join(bb[i:])
# 	break
# print(res)

n=2
# for i in range(n):
k = 6
nums = [4,7,2,9,5,2]
res1 = sum(nums[:k//2])
res2 = sum(nums[k//2:])
print( "case #{}: {} {}".format(1, res1, res2) )

a, b = 1, 3
for i in [a, b]:
	i += 1
print(a, b)



r = int(365)
res = 0
for i in range(0, int(sqrt(r))+1 ):
	a = sqrt( r-i**2 )
	if a == int(a):
		res += 1
		print(i, a)
print( res*4 )


rs = int(365)  
times = 0  
r = sqrt(rs)  
x = 0  
while (x < r):  
	y = int(sqrt(rs - x*x))  
	area = x*x + y*y  
	if area == rs:  
   		times+=1
   		print(x,y)  
	x += 1  

print(times*4)