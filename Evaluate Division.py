import itertools
import collections
class Solution(object):
	def calcEquation(self, equations, values, queries):
		"""
		:type equations: List[List[str]]
		:type values: List[float]
		:type queries: List[List[str]]
		:rtype: List[float]
		"""
		record = collections.defaultdict( dict )
		for (num, den), val in zip(equations, values):
			record[num][num] = record[den][den] = 1
			record[num][den] = val
			record[den][num] = 1/val
		print(repr(record))
		for k in record:
			for i in record[k]:
				for j in record[k]:
					record[i][j] = record[i][k] * record[k][j]
		# print(record)
		return [record[num].get(den, -1.0) for num, den in queries]
		# return [record[num][den] for num, den in queries]
		# dic = {}
		# for i, j in zip(equations, values):
		# 	# print("".join(i), j)
		# 	key = "".join(i)
		# 	dic[ key ] = j
		# 	dic[ key[::-1] ] = 1/j
		# keyList = dic.keys()
		# for i,j in itertools.combinations(keyList, 2):
		# 	if i[-1] == j[0]:
		# 		# if i[0] == j[-1]:
		# 		# 	continue
		# 		key = i[0] + j[-1]
		# 		if key in dic:
		# 			pass
		# 		else:
		# 			dic[key] = dic[i]* dic[j]
		# 			dic[key[::-1]] = 1/dic[key]
		# # print(dic)
		# res = []
		# for i,j in queries:
			
		# 	key = i+j
		# 	if key in dic:
		# 		res.append( dic[key] )
		# 	else:
		# 		res.append( -1.0 )
		# 	# print(i,j,res)
		# return res






equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

sl = Solution()
print( sl.calcEquation( equations, values, queries ) )