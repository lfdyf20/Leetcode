class Solution(object):
	def exclusiveTime(self, n, logs):
		"""
		:type n: int
		:type logs: List[str]
		:rtype: List[int]
		"""
		ans = [0] * n
		stack = []
		prev_time = 0

		for log in logs:
			fn, typ, time = log.split(':')
			fn, time = int(fn), int(time)

			if typ == 'start':
				if stack:
					ans[stack[-1]] += time - prev_time 
				stack.append(fn)
				prev_time = time
			else:
				ans[stack.pop()] += time - prev_time + 1
				prev_time = time + 1

		return ans



n = 8
logs = ["0:start:0",
		"1:start:5",
		"2:start:6",
		"3:start:9",
		"4:start:11",
		"5:start:12",
		"6:start:14",
		"7:start:15",
		"1:start:24",
		"1:end:29",
		"7:end:34",
		"6:end:37",
		"5:end:39",
		"4:end:40",
		"3:end:45",
		"0:start:49","0:end:54","5:start:55","5:end:59","4:start:63","4:end:66","2:start:69","2:end:70","2:start:74","6:start:78","0:start:79","0:end:80","6:end:85","1:start:89","1:end:93","2:end:96","2:end:100","1:end:102","2:start:105","2:end:109","0:end:114"]
# [20,14,35,7,6,9,10,14]
sl = Solution()
print( sl.exclusiveTime( n, logs ) )




## error case
"""
z: start: 1
x: end: 10
y: start: 30

between 10 and 30, x end and y has not started yet, so z is runnning on
the background.
so we need a stack to track last start job who hasn't ended yet!!!!s
"""