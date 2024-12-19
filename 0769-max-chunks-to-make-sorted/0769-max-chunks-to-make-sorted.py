class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans=0
        count=0
        for i in range(len(arr)):
            ans=max(ans, arr[i])
            if ans==i:
                count+=1
        return count
        
        
        
        
        