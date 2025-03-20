class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        groups = [-1] * n
        costs = [-1] * n
        def _get_group(node: int) -> int:
            nonlocal groups
            if groups[node] == -1:
                return node
            g = _get_group(groups[node])
            groups[node] = g
            return g
        for u, v, w in edges:
            gu = _get_group(u)
            gv = _get_group(v)
            if gu == gv:
                costs[gu] &= w
                continue
            cost = w
            if costs[gu] >= 0:
                cost &= costs[gu]
            if costs[gv] >= 0:
                cost &= costs[gv]
            groups[gu] = gv
            costs[gv] = cost
        res = []
        for s, t in query:
            gs = _get_group(s)
            gt = _get_group(t)
            if gs == gt:
                res.append(costs[gs])
            else:
                res.append(-1)
        return res