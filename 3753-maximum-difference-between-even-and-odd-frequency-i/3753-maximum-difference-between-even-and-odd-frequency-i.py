class Solution:
    def maxDifference(self, s: str) -> int:
        q = Counter(s).values()
        return max(v%2*v for v in q)-min(v for v in q if v%2^1)