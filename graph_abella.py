"""
Graph Traversal Program (ABELLA)
Name: ABELLA
Assessment 3.3: Non-Linear Data Structures
"""

from collections import deque


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def bfs(self, start):
        visited = []
        queue = deque([start])
        visited_set = {start}

        while queue:
            node = queue.popleft()
            visited.append(node)
            for neighbor in sorted(self.adj_list.get(node, [])):
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    queue.append(neighbor)
        return visited

    def dfs(self, start, visited=None, visited_set=None):
        if visited is None:
            visited = []
        if visited_set is None:
            visited_set = set()

        visited.append(start)
        visited_set.add(start)

        for neighbor in sorted(self.adj_list.get(start, [])):
            if neighbor not in visited_set:
                self.dfs(neighbor, visited, visited_set)
        return visited


if __name__ == "__main__":
    # Constructing Graph for ABELLA (Vertices: A, B, E, L)
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'E')
    g.add_edge('A', 'L')
    g.add_edge('B', 'E')
    g.add_edge('B', 'L')
    g.add_edge('E', 'L')

    print("--- Graph Traversal (ABELLA) ---")
    print("BFS Traversal:", " -> ".join(g.bfs('A')))
    print("DFS Traversal:", " -> ".join(g.dfs('A')))