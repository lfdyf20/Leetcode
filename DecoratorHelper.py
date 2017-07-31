import time

def timer(func):
	def wrapper(*args, **kv):
		start = time.time()
		res = func( *args, **kv )
		runtime = time.time()-start
		print( "[{func} runtime]:\t {runtime}".format( 
			func=func.__name__,  runtime=runtime) )
		return res
	return wrapper


		