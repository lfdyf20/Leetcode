# n = 9
# nums = [100,100,100,99,99,99,100]
# nums_set = set(nums)
# length = len(nums_set)
# res = []
# for i in range( len(nums) ):
# 	print(nums[~i])
# 	if nums[~i] in nums_set:
# 		res = [ nums[~i] ] + res
# 		nums_set.remove( nums[~i] )
# 	if len(res) == length:
# 		break
# res = [ str(i) for i in res ]
# print(" ".join(res))


# s = "3072 3072 7168 3072 1024"

# nums = sorted([ int(x)/1024 for x in s.strip().split()], reverse=True)

# print( nums )

# ave = sum(nums)/2

# def dp( res1, nums, ave ):
# 	if res1 > ave:
# 		return max(res1, res2+sum(nums))
# 	if res1 + sum(nums) < ave:
# 		return float('inf')
# 	r1 = dp(res1+nums[0], nums[1:], ave)
# 	r2 = dp(res1, nums[1:], ave)
# 	return min( r1, r2 )

# res1, res2 = 0, 0
# res = dp( res1, nums, ave )
# print(res*1024)


# rec = [ [0]*(ave+1) for _ in range(len(nums)+1) ]
# w = len(rec[0])
# n = len(rec)
# print(n,w)
# rec[0][0] == 1
# for i in range(1,n):
# 	for j in range(1,w):
# 		rec[i][j] = rec[i-1][j]
# 		if j > nums[i-1] and rec[i-1][j-nums[i-1]]==1:
# 			rec[i][j]==1
# print(rec)



# n = 3
# s = ["0 50", "1 20", "2 30"]

# num, p = [], []
# for i in range(n):
# 	temp = [int(x) for x in s[i].strip().split()]
# 	num.append( temp[0] )
# 	p.append( temp[1] )

# res = sum( x*y for x,y in zip(num,p) )
# res = res*1.0/sum(p)
# print "%0.3f"%res


#################
s = list('abbccb')

# for i in range(len(s)-1):
# 	for j in range(i+1,len(s)):
# 		if s[i:j]

# res = 0

# from collections import Counter
# for i in range(len(s)-2):
# 	for j in range(i+2, len(s)+1, 2):
# 		counter = Counter(s[i:j])
# 		for k in counter.values():
# 			if k%2!=0:
# 				break
# 		else:
# 			print(s[i:j])
# 			res += 1

# print res


############################
s = "1 2 3 5 6"
N, M = 5, 6
tasks =  [ int(x) for x in s.split() ]
temps = [3,2,1,4,5,6]

temps.sort()

curr = 0
time = []
# for i in range(len(tasks)-1):
# 	if tasks[i+1]-tasks[i]<=1:
# 		continue
# 	for j in range(len(time)):
# 		if time[j]==0 and temps[j]<tasks[i+1]:
# 			time[j]=tasks[i]+1
# else:
# 	i += 1
# 	for j in range(len(time)):
# 		if time[j]==0:
# 			time[j]=tasks[i]+1

for i in xrange(len(tasks)-1):
	if tasks[i+1]-tasks[i] > 1:
		while curr<len(temps) and temps[curr]<tasks[i+1]:
			print(curr, tasks[i+1])
			time.append( tasks[i]+1 )
			curr += 1
while curr < len(temps):
	time.append( tasks[-1]+1 )
	curr += 1
print(time)
