"""
Binary Tree Traversal Program (ABELLA)
Name: ABELLA
Assessment 3.3: Non-Linear Data Structures
"""

from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return []
    visited = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        visited.append(node.key)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited

def dfs_preorder(node, visited=None):
    if visited is None:
        visited = []
    if node:
        visited.append(node.key)
        dfs_preorder(node.left, visited)
        dfs_preorder(node.right, visited)
    return visited

if __name__ == "__main__":
    # Constructing Binary Tree for ABELLA
    # Root: A
    # Level 1: B (left), E (right)
    # Level 2: L (left of B), L (right of B), A (left of E)
    root = Node('A')
    root.left = Node('B')
    root.right = Node('E')
    root.left.left = Node('L')
    root.left.right = Node('L')
    root.right.left = Node('A')

    print("--- Binary Tree Traversal (ABELLA) ---")
    print("BFS (Level Order):", " -> ".join(bfs(root)))
    print("DFS (Pre-Order):", " -> ".join(dfs_preorder(root)))