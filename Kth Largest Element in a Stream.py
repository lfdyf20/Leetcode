from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # No heap solution
        self.k_list = sorted(nums, reverse=True)[:k]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.k_list) < self.k:
            self.k_list.append(val)
            self.k_list.sort(reverse=True)
            if len(self.k_list) == self.k:
                return self.k_list[-1]
        
        for i in range(len(self.k_list)-1, -1, -1):
            if val < self.k_list[i]:
                self.k_list.insert(i+1, val)
                self.k_list.pop(-1)
                break
        else:
            self.k_list.insert(0, val)
            self.k_list.pop(-1)
        return self.k_list[-1]
        


k = 3
nums = [5, -1]
obj = KthLargest(k, nums)
print(obj.add(-3)) # 
print(obj.add(-2)) #
print(obj.add(-4)) #
print(obj.add(0)) #
print(obj.add(4)) #