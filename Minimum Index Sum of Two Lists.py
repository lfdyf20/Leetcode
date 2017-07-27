from collections import defaultdict
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if len(list1) > len(list2):
        	return self.findRestaurant(list2, list1)

        dict = {}
        res, score = [], float('inf')
        for i, name in enumerate(list1):
        	dict[name] = i
        for i, name in enumerate(list2):
        	if name in dict:
        		if dict[name] + i == score:
        			res.append(name)
        		elif dict[name] + i < score:
        			res = [ name ]
        			score = dict[name] + i
        return res





        # dict = {}
        # res, score = [], float('inf')
        # for i, names in enumerate(zip(list1, list2)):
        # 	for name in names:
        # 		if name in dict:
        # 			if dict[name] + i == score:
        # 				res.append(name)
        # 			elif dict[name] + i < score:
        # 				res = [ name ]
        # 				score = dict[name] + i
        # 		else:
        # 			dict[name] = i
        # print(dict)
        # return res



list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]


sl = Solution()
print( sl.findRestaurant( list1, list2 ) )