from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = Counter(tasks)
        counts = d.values()
        longest = max(counts)
        ans = (longest - 1) * (n + 1)
        for count in counts:
            ans += count == longest and 1 or 0
        return max(len(tasks), ans)


# https://leetcode.com/problems/task-scheduler/Figures/621_Task_Scheduler_new.PNG

tasks = ['A','A','A','B','B','B']
n = 2
sl = Solution()
print( sl.leastInterval( tasks, n ) )