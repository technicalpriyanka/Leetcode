class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values=[0]*(len(grid)**2+1)
        for i in range(len(grid)):
            for j in range(len(grid)):
                values[grid[i][j]]+=1
        res=[0,0]
        for i in range(1,len(grid)**2+1):
            if values[i]==2:
                res[0]=i
            elif values[i]==0:
                res[1]=i
        return res