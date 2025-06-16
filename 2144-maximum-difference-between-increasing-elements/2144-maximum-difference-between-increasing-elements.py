class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        less = nums[0]
        for i in range(1, len(nums)):
            less = min(less, nums[i])
            if nums[i] > less:
                ans = max(ans, nums[i] - less)
        return ans        