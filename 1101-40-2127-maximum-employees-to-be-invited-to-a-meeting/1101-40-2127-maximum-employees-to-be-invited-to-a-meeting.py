class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)

        # Step 1: Calculate indegree for topological sorting
        indeg = [0] * n
        for i in range(n):
            indeg[favorite[i]] += 1

        # Step 2: Initialize queue for nodes with indegree 0
        used = [False] * n
        f = [1] * n
        q = deque(i for i in range(n) if indeg[i] == 0)

        # Topological sorting and chain length calculation
        while q:
            u = q.popleft()
            used[u] = True
            v = favorite[u]
            f[v] = max(f[v], f[u] + 1)  # Update the longest chain ending at v
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

        # Step 3: Analyze cycles
        ring = 0
        total = 0

        for i in range(n):
            if not used[i]:  # Node i is part of a cycle
                j = favorite[i]
                if favorite[j] == i:  # 2-node cycle
                    total += f[i] + f[j]  # Sum chain lengths for the 2-node cycle
                    used[i] = used[j] = True
                else:  # Larger cycles
                    u = i
                    cnt = 0
                    while True:
                        cnt += 1
                        u = favorite[u]
                        used[u] = True
                        if u == i:  # Cycle complete
                            break
                    ring = max(ring, cnt)  # Update largest cycle size

        # Step 4: Return the result
        return max(ring, total)