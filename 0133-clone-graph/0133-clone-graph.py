"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def dfs(n):
            if n in oldToNew:
                return oldToNew[n]
            new = Node(n.val)
            oldToNew[n] = new

            for neighbor in n.neighbors:
                new.neighbors.append(dfs(neighbor))
            return new

        return dfs(node) if node else None
        


        