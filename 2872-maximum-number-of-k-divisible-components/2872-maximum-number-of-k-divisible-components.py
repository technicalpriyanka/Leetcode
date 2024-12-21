class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        connect = defaultdict(list)

        for i,j in edges:
            connect[i].append(j)
            connect[j].append(i)
        visted = set()
        res = 0
        def dfs(num):
            nonlocal visted,res,k
            visted.add(num)
            total = 0 
            for i in connect[num]:
                if i not in visted:
                    total+=dfs(i)
            if (total +values[num])%k==0:
                res+=1
                return 0
            else:
                return total +values[num]
        
        dfs(0)
        return res
        