class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0
        
        if (total_sum + target) %2:
            return 0
        
        subset1 = (total_sum + target) //2

        dp=[[0] * (subset1 + 1) for _ in range(len(nums)+1)]
        dp[0][0] =1

        for i in range(1, len(nums)+1):
            for j in range(subset1 + 1):
                dp[i][j] = dp[i-1][j]
                
                if j-nums[i-1] >= 0:
                    dp[i][j] = dp[i][j] + dp[i-1][j-nums[i-1]]
                    
        return dp[-1][-1]

        