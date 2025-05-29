class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])

        for i in range(numRows - 1):
            newRow = [1]
            for j in range(i):
                newRow.append(ans[i][j] + ans[i][j+1])
                
            newRow.append(1)
            ans.append(newRow)


        return ans