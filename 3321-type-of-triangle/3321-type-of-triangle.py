class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0]+nums[1]<=nums[2] or nums[1]+nums[2]<=nums[0] or nums[0]+nums[2]<=nums[1]:
            return 'none'
        else:
            k=set(nums)
            if len(k)==1:
                return 'equilateral'
            elif len(k)==2:
                return 'isosceles'
            else:
                return 'scalene'
            
            