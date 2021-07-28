class Solution:
    def insert(self, intervals, newInterval):
        res = []
        leftIndex = rightIndex = 0
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval=[min(newInterval[0],interval[0]),max(newInterval[1],interval[1])]
        res.append(newInterval)

        return res

        




intervals =  [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]


sl = Solution()
print( sl.insert( intervals, newInterval ) )