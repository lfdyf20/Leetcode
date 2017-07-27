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


a = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
for string in a:
    match = re.search(r"(?P<path>.*) (?P<name>.*)(?:\(.*\))", string)
    filepath, filename = match.group('path','name')
    print(filename, filepath)