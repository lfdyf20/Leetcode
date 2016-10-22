#encoding:utf-8
"""try new functions and features
""" 
import re
import logging
import json
import os
from multiprocessing import Process
from collections import namedtuple
from collections import defaultdict
from collections import Counter
import hashlib

import numpy as np

class Solution(object):

	def regex(self, str):
		"""
		
		regular expression
		
		Arguments:
			str {[string]} -- "Hello .ben@forta.com is my email address."
		return:
			result {[string]} -- [the text found]
		"""
		match = re.search("(\w+[\w.]*)@[\w.]+(\.\w+)", str)
		print("1:", match.group() if match != None else "no match")
		
		pattern = re.compile("[\w.]*@[\w.]+\.\w+")
		match = pattern.search( str )
		print( "2:",  match.group() if match != None else "no match")

		match = re.search("\.en", str)
		print( "3:",  match.group() if match != None else "no match")

		match = re.findall("hello", str) # type( match) = list
		print( "4:", match if match != None else "no match")

		match = re.sub("he\w{3}", "fei", str)
		print( "5:", match)

		match = re.search("(he).*?(lo)", str)
		print( "6:", match.groups() if match != None else "no match")

		match = re.search(r"(is).(?=\1)", str)
		print( "7:", match.group() if match != None else "no match")

		return "Over"


	def unicode(self):
		print( "你好" )
		print( ord("H") )
		print( chr(40) )
		s = u"中文".encode("utf-8")
		print(s)

	def raiseError(self):
		raise AttributeError("OMG, at least give me one attribute please")
		raise TypeError("and it should be a number")

	def function(self, x, y=10, **attribute):
		print( x+y )
		print( "x:",x, "y:",y, "attribute:",attribute )

	
	"""
	import logging to log error exception
	"""
	def tryError(self, a, b):
		try:
			print( "result:", a/b )
		except ZeroDivisionError as e:
			logging.exception(e)
			print( a*b )
		else:
			print("no error")
		finally:
			print("finally")
	

	"""[summary]
	r:file like object;
	rb: pictures media binery files
	w: write files
	"""
	def readFiles(self, path):
		with open( path, "r" ) as f:  #use with to avoid using f.close()
			for line in f.readlines():
				print(line.strip())

	#import json
	def useJson(self, path):
		# with open( path, "a+") as f:
		# 	d = dict( name = "fei", age = "27")
		# 	str_d = json.dumps(d)
		# 	json.dump(d, f)
		# 	dd = json.loads( str_d )
		# 	print dd
		with open(path, "r") as f:
			dic = json.load(f)
			print( dic )

	#import os
	def multiProcess(self):
		print('Process (%s) start...' % os.getpid())
		pid = os.fork()
		if pid==0:
			print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
		else:
			print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

	#from multiprocessing import Process
	def multiProcess2(self):
		def run_proc(name):
			print('Run child process %s (%s)...' % (name, os.getpid()))
		
		print('Parent process %s.' % os.getpid())
		p = Process(target=run_proc, args=('test',))
		print('Process will start.')
		p.start()
		p.join()
		print('Process end.')


	# from collections import namedtuple
	# from collections import defaultdict
	# from collections import Counter
	def builtInModule(self, module):
		if module == "namedtuple":
			Point = namedtuple("Point",["x", "y"])
			p = Point(1, 2)
			print('the point',p, 'is at', p.x, p.y)
		elif module == "defaultdict":
			dd = defaultdict(lambda:"N/A")
			dd["key1"] = "value1"
			print(dd['key1'], dd['key2'])
		elif module == "Counter":
			c = Counter()
			for ch in "Hello My Name is Fei":
				c[ch] = c[ch] + 1
			print(c)


	# import hashlib
	def hashlibFun(self):
		a = ["hello", "world"]
		b = ["hello", "word"]
		c = "hello world"
		d = "helloworld"
		e = "hello word"
		md5_a = hashlib.md5()
		md5_b = hashlib.md5()
		md5_c = hashlib.md5()
		md5_d = hashlib.md5()
		md5_e = hashlib.md5()
		for i in a:
			md5_a.update(i)
		for i in b:
			md5_b.update(i)
		md5_c.update(c)
		md5_d.update(d)
		md5_e.update(e)
		print( md5_a.hexdigest(),"\n", md5_b.hexdigest(),'\n',md5_c.hexdigest(),"\n",md5_d.hexdigest(),"\n",md5_e.hexdigest() )

	def returnMulVal(self):
		return 1, 2


	#import numpy as np
	def tryNumpy(self):
		x = [1,2,3]
		y = [1,3,4]
		xArray = np.array( x )
		yArray = np.array( y )
		# res = xArray * yArray
		# res = res.sum()
		res = xArray.dot( yArray )
		print( type(res) )
		return res


	#try input
	def tryArg(self, *args):
		for i in args:
			print(i)

	def tryArgs(self, **args ):
		for i in args:
			print( i, args[i] )





	
	



