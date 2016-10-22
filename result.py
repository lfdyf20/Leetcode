from tryFunc import Solution

sample = Solution()


#----- regex expression
# str = "Hello .ben@forta.com is my email address."
# str = " hello world <it is is a joke> and hello"
# print sample.regex(str)

#----- unicode
# sample.unicode()


#----- raise error
# sample.raiseError()

#----- function
# sample.function(10,1, age=100, city="jurong")

#----- try except else finally
# sample.tryError(1,0)

#----- read files
# sample.readFiles( "try.txt" )

#----- json
# sample.useJson("try2.json")

#----- multi Process
# sample.multiProcess()
# sample.multiProcess2()

#----- built-in module
# sample.builtInModule("namedtuple")
# sample.builtInModule("defaultdict")
# sample.builtInModule("Counter")

#----- hashlib
# sample.hashlibFun()

#----- return multipy values
# val1 = sample.returnMulVal()
# print(val1)

#----- numpy
# print( sample.tryNumpy() )

#----- *args , **args
# print( sample.tryArg(1,2,3,4) )
print( sample.tryArgs(name = 'Fei', age = '3') )