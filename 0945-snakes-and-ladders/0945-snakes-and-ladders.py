class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # Flatten the board to 1D array
        flattened = [0] * (n * n + 1)  # 1-based indexing
        for i in range(n):
            for j in range(n):
                # Calculate position in flattened array
                row = n - 1 - i
                if (n - i) % 2 == 0:
                    col = n - 1 - j
                else:
                    col = j
                pos = row * n + col + 1
                flattened[pos] = board[i][j]
        
        # BFS initialization
        queue = deque([1])
        visited = [False] * (n * n + 1)
        visited[1] = True
        steps = 0
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                # Explore all 6 possible moves
                for move in range(1, 7):
                    next_pos = current + move
                    if next_pos > n * n:
                        continue
                    # Check for snake or ladder
                    dest = flattened[next_pos] if flattened[next_pos] != -1 else next_pos
                    if dest == n * n:
                        return steps
                    if not visited[dest]:
                        visited[dest] = True
                        queue.append(dest)
        return -1