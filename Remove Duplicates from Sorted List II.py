# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        dummy = pre = ListNode(0)
        dummy.next =head
        while head and head.next:
        	if head.val == head.next.val:
        		while head and head.next and head.val == head.next.val:
        			head = head.next
        		head = head.next
        		pre.next = head
        	else:
        		pre = pre.next
        		head = head.next
        return dummy.next









def show(head):
	while head:
		print(head.val, end='')
		head = head.next
	print('')


x = [1,1,2,2,3,4,4,5]
if not x:
	head = None
else:
	head = curr = ListNode(x[0])
	for i in x[1:]:
		curr.next = ListNode(i)
		curr = curr.next

show(head)

sl = Solution()
head = sl.deleteDuplicates(head)
show( head )