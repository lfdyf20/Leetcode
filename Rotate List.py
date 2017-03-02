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
        return newHead


    def mySolution(self, head, k):
        if not head: return
        if not head.next or not k: return head
        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1
        k = k % n
        if k==0: return head
        fast = slow = head
        while k>0:
            try:
                fast = fast.next
                k -= 1
            except:
                return head
        if not fast:
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        newHead, fast.next, slow.next = slow.next, head, None
        return newHead



def showLinkedList(head):
    while head:
        print(head.val, end='')
        head = head.next
    print('\n')


k = 2
nodes = [1,2]
if len(nodes):
    head = ListNode( nodes[0] )
    curr = head
    for i in nodes[1:]:
        curr.next = ListNode(i)
        curr = curr.next
else:
    head = None


sl = Solution()


head = sl.mySolution(head, k)
showLinkedList(head)
