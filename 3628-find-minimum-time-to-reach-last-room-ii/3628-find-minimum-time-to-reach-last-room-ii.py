from heapq import *

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        seen = set()
        
        def get_neighbours(x, y):
            candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            neigh = []
            for p,q in candidates:
                if p<0 or p>=n or q<0 or q>=m:
                    continue
                neigh.append((p,q))
            return neigh

        
        dist = [[10**10] * (m) for _ in range(n)]
        dist[0][0] = 0
        que = [(0, 0, 0, 0)]
        while que:
            elapsed, x, y, parity = heappop(que)
            if x == n-1 and y == m-1:
                break
            if (x,y, parity) in seen:
                continue
            seen.add((x,y, parity))
            for p,q in get_neighbours(x, y):
                new_elapsed = max(elapsed, elapsed + (moveTime[p][q]-elapsed))
                new_dist = new_elapsed + (2 if parity else 1)
                if new_dist < dist[p][q]:
                    dist[p][q] = new_dist
                    heappush(que, (new_dist, p, q, (1-parity)))
        
            
        return dist[n-1][m-1]