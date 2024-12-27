class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans=0
        t=values[0]+0
        for i in range(1, len(values)):
            ans=max(ans, t+values[i]-i)
            t=max(t, values[i]+i)
        return ans
        
    
        