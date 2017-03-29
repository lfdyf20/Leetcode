# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """ 
        dummy1 = curr1 = ListNode(0)
        dummy2 = curr2 = ListNode(0)
        while head:
        	if head.val < x:
        		curr1.next = ListNode(head.val)
        		curr1 = curr1.next
        	else:
        		curr2.next = ListNode(head.val)
        		curr2 = curr2.next
        	head = head.next
        show(dummy1)
        show(dummy2)
        curr1.next = dummy2.next
        show(dummy1)
        return dummy1.next








def show(head):
	while head:
		print(head.val, end='')
		head = head.next
	print('')


numlist, x = [1,4,3,2,5,2], 3
if not numlist:
	head = None
else:
	head = curr = ListNode(numlist[0])
	for i in numlist[1:]:
		curr.next = ListNode(i)
		curr = curr.next

show(head)

sl = Solution()
head = sl.partition(head, x)

show(head)
