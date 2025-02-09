class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # equivalent to: i - nums[i] != j - nums[j]
        m = defaultdict(int)

        for i, num in enumerate(nums):
            m[i - num] += 1
        
        n = len(nums)
        res = n * (n - 1) // 2
        
        for v in m.values():
            res -= v * (v - 1) // 2
        
        return res