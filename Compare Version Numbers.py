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

    def mySolution(self, version1, version2):
        v1 = list(map(int,version1.split(".")))
        v2 = list(map(int,version2.split(".")))

        while v1 and v1[-1] == 0:
            v1.pop()
        while v2 and v2[-1] == 0:
            v2.pop()

        for i,j in zip(v1, v2):
            if i > j:
                return 1
            if i < j:
                return -1
        else:
            if len(v1) > len(v2):
                return 1
            elif len(v1) < len(v2):
                return -1
            else:
                return 0






version1 = "4.08"
version2 = "4.08.01"

version1, version2 = "1.0", "1"

sample = Solution()
print(sample.compareVersion(version1, version2))
print(sample.mySolution(version1,version2))