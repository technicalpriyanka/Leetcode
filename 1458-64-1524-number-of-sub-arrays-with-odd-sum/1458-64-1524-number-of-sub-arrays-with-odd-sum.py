class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod, n = 10 ** 9 + 7, len(arr)
        x, y, cummulative_sum, res = 0, 1, 0, 0
        for num in arr:
            cummulative_sum += num # check if sum up to current index is even or odd
            if cummulative_sum % 2 == 1: # if sum is odd, up to y number of arrays will become odd
                x += 1
                res += y % mod
            else: #if sum is even, up to x number of arrays will become odd
                y += 1
                res += x % mod
        res %= mod
        return res