import re
import os

# fileName = "Number of Islands.py"
fileName = max([f for f in os.listdir('.') if re.match(r'[\w ]*\.py', f)], key = os.path.getctime)
print( fileName )
with open( fileName, 'r' ) as f:
	content = f.read()


match = re.search("def (\w+)\(self, ([, \w]+)\)", content)
matchSL = re.search("sl.=.Solution", content)
# print(matchSL.groups())
if matchSL == None:
	funcName = match.group(1)
	varName = match.group(2)
	contentToAdd = "\n\n\n\n"
	contentToAdd += varName + " = \n\n"
	contentToAdd += "sl = Solution()\n"
	contentToAdd += "print( sl." + funcName + "( " + varName+ " ) )" 
	with open( fileName, 'a' ) as f:
		f.write(contentToAdd)

