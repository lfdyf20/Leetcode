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



equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

sl = Solution()
print( sl.calcEquation( equations, values, queries ) )