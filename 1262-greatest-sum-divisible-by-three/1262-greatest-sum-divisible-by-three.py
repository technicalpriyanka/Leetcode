class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans=sum(nums)
        if ans % 3 == 0:
            return ans

        a1 = list()
        a2 = list()

        for n in nums:
            if n%3 == 1:
                a1.append(n)
            elif n%3 == 2:
                a2.append(n)
            
        a1.sort()
        a2.sort()

        candidates = [0]
        if ans % 3 == 1:
            if a1:
                candidates.append(ans - a1[0])

            if len(a2) >= 2:
                candidates.append(ans - a2[0] - a2[1])

        else:
            if a2:
                candidates.append(ans - a2[0])

            if len(a1) >= 2:
                candidates.append(ans - a1[0] - a1[1])

        return max(candidates)

        