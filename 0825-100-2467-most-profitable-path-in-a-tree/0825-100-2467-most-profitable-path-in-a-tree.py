class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        prev = {0: 0}
        def findBob(node, visited):
            if node == bob: return True

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    
                    prev[nei] = node
                    if findBob(nei, visited):
                        return True
            return False
        
		# find Bob's path
        findBob(0, set([0]))
        
        maxIncome = float("-inf")
        def dfs(state, node, visited, bobNode, path): 
            nonlocal maxIncome
            
            if node == bobNode:
                state += amount[node]//2
            else:
                if node not in path:
                    state += amount[node]
                    
            nexts = set(graph[node])
            if len(nexts) == len(nexts & visited): # reach leaf node
                maxIncome = max(maxIncome, state)
                return

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    path.add(bobNode)
                    dfs(state, nei, visited, prev[bobNode], path)
                    path.discard(bobNode) # backtracking
            return
        
        dfs(0, 0, set([0]), bob, set())
        return maxIncome 