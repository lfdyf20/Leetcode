class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k==0 :
            return head
        n = 1
        curr = head
        while curr.next:
        	curr = curr.next
        	n += 1
        curr.next = head
        # print(curr.val, n)

        k = k % n
        rotInd = n - k
        curr = head
        
        for i in range(1, rotInd):
        	curr = curr.next
        # print(curr.val)
        newHead = curr.next
        curr.next = None
        return newHead.val

head = ListNode(1)
curr = head
for i in range(1,5):
	curr.next = ListNode(i+1)
	curr = curr.next


k = 2
sl = Solution()
print( sl.rotateRight( head, k ))

# curr = head
# for i in range( 1,6 ):
# 	print( curr.val )
# 	curr = curr.next