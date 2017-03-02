# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        nodeHeap = []
        # nodeHeap = [ (node.val, node) for node in lists if node ]
        # heapq.heapify(nodeHeap)
        for node in lists:
        	heapq.heappush( nodeHeap, (node.val, node) )
        while nodeHeap:
        	nodeVal, node = nodeHeap[0]
        	if not node.next:
        		heapq.heappop( nodeHeap )
        	else:
        		heapq.heapreplace( nodeHeap, (node.next.val, node.next) )
        	curr.next = node
        	curr = curr.next

        return dummy.next





nodelists = [[1,11,111], [2,22],[0,7]]

x = []

for nodelist in nodelists:
	dummy = curr = ListNode(0)
	for nodeVal in nodelist:
		curr.next = ListNode( nodeVal )
		curr = curr.next
	x.append( dummy.next )

sl = Solution()
head = sl.mergeKLists( x )
while head:
	print(head.val)
	head = head.next