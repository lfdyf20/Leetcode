class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for entry in paths:
        	x = entry.split()
        	path, files = x[0], x[1:]
        	for file in files:
        		name, content = file.split('(')
        		if content[:-1] in dic:
        			dic[content[:-1]].append(path + '/' + name)
        		else:
        			dic[content[:-1]] = [path + '/' + name]
        return [x for x in dic.values() if len(x)>1]



paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

sl = Solution()
print( sl.findDuplicate( paths ) )