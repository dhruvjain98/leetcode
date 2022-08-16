"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        o2n = {}
        def dfs(node):
            if node in o2n:
                return o2n[node]
            
            copy = Node(node.val)
            o2n[node] = copy
            
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node) if node else None