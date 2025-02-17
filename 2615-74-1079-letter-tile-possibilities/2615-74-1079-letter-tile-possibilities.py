class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        dic = Counter(tiles)

        def backtrack(idx, n, freq):
            if idx == n:
                return 1
            ways = 0
            for i in freq:
                if freq[i] > 0:
                    freq[i] -= 1
                    ways += backtrack(idx+1, n, freq)
                    freq[i] += 1

            return ways
        
        res = 0
        N = len(tiles)
        for i in range(1, N + 1):
            res += backtrack(0, i, dic)
        return res