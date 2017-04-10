class Human(object):
	"""docstring for Human"""
	def __init__(self, name, **kw):
		# super(Human, self).__init__()
		self.__name = name
		self.__gender = kw["gender"] if "gender" in kw else None
		self.__age = kw["age"] if "age" in kw else None

	def showInfo(self):
		print("name: ", self.__name)
		print("gender: ", self.__gender)
		print("age: ",self.__age)
	

class Student(Human):
	"""docstring for Student"""
	def __init__(self,name, **kw):
		# Human.__init__(self,name, **kw)
		super().__init__(name, **kw)
		self.__score = kw["score"] if "score" in kw else None

	def showInfo(self, **kw):
		super().showInfo()
		print("score: ",self.__score)

	def validate(self):
		print("[Validation] This is a student")

	






jack = Human("Jack", gender="male", age=16)
jack.showInfo()

hello = Student("hello", gender="female", age=18, score=87)
hello.showInfo()

hello.validate()
