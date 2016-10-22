class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int,version1.split("."))
        v2 = map(int,version2.split("."))
        print "v1=",v1, "\n", "v2=",v2
        if len(v1) < len(v2):
            v1.extend([0]*(len(v2)-len(v1)))

        else:
            print v2.extend([0]*(len(v1)-len(v2)))
        return cmp(v1,v2)





version1 = "1.2"
version2 = "1.1"
sample = Solution()
print sample.compareVersion(version1, version2)