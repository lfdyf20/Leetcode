import re
import os


# Settings:
USE_CREATION_TIME = False


fileName = max([f for f in os.listdir('.') if re.match(r'[\w ]*\.py', f)], 
	key = os.path.getctime if USE_CREATION_TIME else os.path.getmtime)
print( fileName )
with open( fileName, 'r' ) as f:
	content = f.read()

	match = re.search("def ([\w\d]+)\(self, ([\w\d: \[\],]+)\)", content)
	matchSL = re.search("sl.=.Solution", content)
	# print(matchSL.groups())
	if matchSL == None and match:
		funcName = match.group(1)
		parameterInfos = match.group(2)
		contentToAdd = "\n\n\n\n"

		# add parameterInfo
		parameterNames = []
		for var in parameterInfos.split(", "):
			parameterName = var.split(":")[0]
			contentToAdd += parameterName + " = \n"
			parameterNames.append(parameterName)

		contentToAdd += "\n\n"
		contentToAdd += "sl = Solution()\n"
		contentToAdd += "print( sl." + funcName + "( " + ", ".join(parameterNames)+ " ) )" 
		with open( fileName, 'a' ) as f:
			f.write(contentToAdd)

