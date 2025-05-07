class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        
        INF = 10**18
        dist = [[INF] * m for _ in range(n)]
        
        pq = [(0, 0, 0)]
        dist[0][0] = 0
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while pq:
            t, i, j = heapq.heappop(pq)
            if t > dist[i][j]:
                continue

            if i == n-1 and j == m-1:
                return t
            
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    new_time = max(t, moveTime[ni][nj]) + 1
                    if new_time < dist[ni][nj]:
                        dist[ni][nj] = new_time
                        heapq.heappush(pq, (new_time, ni, nj))
        
        return dist[n-1][m-1]          