from LinkedList import LinkedList

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h1 = l1
        v1 = 0
        while h1:
        	v1 = v1*10 + h1.val
        	h1 = h1.next
        h2 = l2
        v2 = 0
        while h2:
        	v2 = v2*10 + h2.val
        	h2 = h2.next
        val = str(v1 + v2)
        dummy = curr = ListNode(0)
        for i in val:
        	curr.next = ListNode(int(i))
        	curr = curr.next
        return dummy.next




l11, l22 = [7,2,4,3] , [5,6,4]
l1 = LinkedList(l11).getHead()
l2 = LinkedList(l22).getHead()



sl = Solution()
head = sl.addTwoNumbers( l1, l2 )
LinkedList([1]).printLinkedList(head)