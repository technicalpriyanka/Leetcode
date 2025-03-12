class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative_count = bisect.bisect_left(nums, 0)
        positive_count = len(nums) - bisect.bisect_right(nums, 0)

        return max(negative_count, positive_count)

        