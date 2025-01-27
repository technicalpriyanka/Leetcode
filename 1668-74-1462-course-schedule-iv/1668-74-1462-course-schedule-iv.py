class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        n = numCourses
        hasPrereq = [0 for _ in range(n)]
        inDegree = [0 for _ in range(n)]
        adjList = defaultdict(list)

        for a, b in prerequisites:
            inDegree[b] += 1
            adjList[a].append(b)
        
        q = deque()
        for i in range(n):
            if inDegree[i] == 0:
                q.append(i)
        
        # O(n^2): For each node, for each edge of node, fill in prereq
        while q:
            currNode = q.popleft()
            for nextNode in adjList[currNode]:
                hasPrereq[nextNode] = hasPrereq[nextNode] | hasPrereq[currNode] # Next course has all the preqrequisites of current course
                hasPrereq[nextNode] = hasPrereq[nextNode] | (1 << currNode) # Next course has current course as a prequisite

                inDegree[nextNode] -= 1
                if inDegree[nextNode] == 0: # If next node has no more prequisites to fill add to queue
                    q.append(nextNode)
        
        ans = []
        for u, v in queries:
            ans.append(hasPrereq[v] & (1 << u) != 0) # Check if u bit is set
        return ans