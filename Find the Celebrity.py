# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        



        









"""
Brilliant algorithm. For those who have problem understanding it, the following is my understanding:

The first loop is to find the candidate as the author explains. In detail, suppose the candidate after the first for loop is person k, it means 0 to k-1 cannot be the celebrity, because they know a previous or current candidate. Also, since k knows no one between k+1 and n-1, k+1 to n-1 can not be the celebrity either. Therefore, k is the only possible celebrity, if there exists one.

The remaining job is to check if k indeed does not know any other persons and all other persons know k.

To this point, I actually realize that we can further shrink the calling of knows method. For example, we don't need to check if k knows k+1 to n-1 in the second loop, because the first loop has already done that.

https://discuss.leetcode.com/topic/23534/java-solution-two-pass/14
"""