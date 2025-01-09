class Solution:
    def countPrimes(self, num: int) -> int:
        count = 0
        ans = [True] * (num+1)
        for i in range(2, int(num**0.5)+1):
            if ans[i]:
                for multiply in range(i*i, num+1, i):
                    ans[multiply]=False
                
        for i in range(2, num):
            if ans[i]:
                count+=1

        return count 