# coding: utf-8
from collections import Counter, defaultdict, deque
from itertools import combinations
import numpy as np
import time
import sys
import random
from math import sqrt
from numpy.linalg import inv
import re
from datetime import datetime
from LinkedList import LinkedList


def subsetsWithDup( nums):
    res = []
    nums.sort()
    dfs(nums, 0, [], res)
    return res
    
def dfs(nums, index, path, res):
    res.append(path)

    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i-1]:
            continue
        dfs(nums, i+1, path+[nums[i]], res)

nums = [1,2,2,3]
print( subsetsWithDup(nums))


a = {"123": 123,
	 "222": 233}
print(a)

print(int('-5'))

a = [1,2,3,4,5]
print(all(x<4 for x in a))

print(int(11.9))

a = 123
b = 222
a, b = b, a
print(a, b)