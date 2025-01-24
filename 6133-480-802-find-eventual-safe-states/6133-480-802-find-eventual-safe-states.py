class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        out = []

        def dfs(i: int) -> bool:
            if graph[i] == []:
                return True
            if i in visited:
                return False
            
            visited.add(i)
            for node in graph[i]:
                if not dfs(node):
                    return False
            
            graph[i] = []
            return True

        for i in range(len(graph)):
            if dfs(i):
                out.append(i)

        return out     