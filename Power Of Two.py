n=16
m=2

def devide(n,m):
	print "n=", n
	if n==1:
		return True
	if n % m == 0:
		return devide(n/m, m)
	else:
		return False

print devide(n,m)
