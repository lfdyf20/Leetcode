import collections
a = [[1,2],[3,4]]
for i in range(2):
	b = list(map(lambda x:x[i], a))
	print(b)

a = (1,2)[True]
print(a)

a = "abcdea"
a = collections.Counter(a)
b = "abba"
b = collections.Counter(b)
print(a&b)