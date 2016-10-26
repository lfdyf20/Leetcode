people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
for p in sorted( people, key = lambda x: (-x[0], x[1]) ):
	print(p)


print(3!)