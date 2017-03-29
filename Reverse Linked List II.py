# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m >= n:
        	return head

        ohead = dummy = ListNode(0)
        whead = wtail = head
        dummy.next = head

        for _ in range(n-m):
        	wtail = wtail.next

        for _ in range(m-1):
        	ohead, whead, wtail = ohead.next, whead.next, wtail.next

        otail, wtail.next = wtail.next, None

        revhead, revtail = self.reverse(whead)

        ohead.next, revtail.next = revhead, otail

        return dummy.next

    def reverse(self, head):
    	pre, curr, tail = None, head, head
    	while curr:
    		curr.next, pre, curr = pre, curr, curr.next
    	return pre, tail





# show nodes.val in the linked list
def showLinkedList(head):
	while head:
		print(head.val, end='')
		head = head.next
	print('')

# generate linked list from list
x = [1,2,3,4,5]
if not x:
	head = None
else:
	head = curr = ListNode(x[0])
	for i in x[1:]:
		curr.next = ListNode(i)
		curr = curr.next

m, n = 2,4

sl = Solution()
head = sl.reverseBetween(head,m,n)
showLinkedList(head)