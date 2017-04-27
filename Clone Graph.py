# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
    	if not node:
    		return
    	nodeCopy = UndirectedGraphNode(node.label)
    	dic = {node:nodeCopy}
    	quene = deque( [node] )
    	while quene:
    		node = quene.popleft()
    		for neighbor in node.neighbors:
    			if neighbor not in dic:
    				neighborCopy = UndirectedGraphNode( neighbor.label )
    				dic[neighbor] = neighborCopy
    				dic[node].neighbors.append( neighborCopy )
    				quene.append(neighbor)
    			else:
    				dic[node].neighbors.append( dic[neighbor] )
    	return nodeCopy