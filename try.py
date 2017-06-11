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


a = LinkedList([1,2,3,4,5])
a.printLinkedList()
# b = a.reverse()
# a.reverseBetween(1,5)
a.removeAt(1)
a.printLinkedList()
a = [1]
a += [a[0]*1]
print(a)

