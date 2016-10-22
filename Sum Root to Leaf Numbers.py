a = [[1,2],[1,2,3,4]]
b = 12+1234

sumVal = 0
for i in a:
	strNum = ''.join(str(e) for e in i)
	num = int(strNum)
	sumVal += num
print( sumVal == b )
