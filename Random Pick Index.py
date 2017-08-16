class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        indexes = self.indexes = {}
        for i, num in enumerate(nums):
            I = indexes.get(num)
            if I is None:
                indexes[num] = i
            elif isinstance(I, int):
                indexes[num] = [I, i]
            else:
                indexes[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """ 
        I = self.indexes[target]
        return I if isinstance(I, int) else random.choice(I)