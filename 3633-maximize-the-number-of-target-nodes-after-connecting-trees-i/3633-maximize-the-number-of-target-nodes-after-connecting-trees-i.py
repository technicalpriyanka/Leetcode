class Solution:
    def count_neighbors(self, source: int, adj_list: list[list[int]], k: int) -> int:
        seen: set[int] = set()
        cur_nodes: list[int] = [source]
        seen.add(source)
        next_nodes: list[int] = []
        length: int = 0
        neighbors: int = 0
        while cur_nodes and length <= k:
            for node in cur_nodes:
                neighbors += 1
                for neighbor in adj_list[node]:
                    if neighbor in seen: continue
                    seen.add(neighbor)
                    next_nodes.append(neighbor)
            cur_nodes = next_nodes
            next_nodes = []
            length += 1
        return neighbors
        
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n: int = len(edges1) + 1
        m: int = len(edges2) + 1
        adj_list_edges1: list[list[int]] = [[] for _ in range(n)]
        adj_list_edges2: list[list[int]] = [[] for _ in range(m)]
        for u, v in edges1:
            adj_list_edges1[u].append(v)
            adj_list_edges1[v].append(u)
        for u, v in edges2:
            adj_list_edges2[u].append(v)
            adj_list_edges2[v].append(u)
        extra: int = 0
        for vertex in range(m):
            extra = max(extra, self.count_neighbors(vertex, adj_list_edges2, k - 1))
        output: list[int] = [0] * n
        for vertex in range(n):
            output[vertex] = self.count_neighbors(vertex, adj_list_edges1, k) + extra
        return output