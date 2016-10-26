class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int,version1.split(".")))       
        v2 = list(map(int,version2.split(".")))
        if len(v1) < len(v2):
            v1.extend([0]*(len(v2)-len(v1)))
        else:
            v2.extend([0]*(len(v1)-len(v2)))
        return (v1>v2)-(v1<v2)





version1 = "4.08"
version2 = "4.08.01"
sample = Solution()
print(sample.compareVersion(version1, version2))
# print(sample.comp(version1,version2))