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



from DecoratorHelper import timer

@timer
def aaa():
    print("aaa")

aaa()

a = sorted(["cata", "bat", "rat"],key=len)
print(a)

a = {"1":2}
print(a.setdefault("2",3))
print(a)