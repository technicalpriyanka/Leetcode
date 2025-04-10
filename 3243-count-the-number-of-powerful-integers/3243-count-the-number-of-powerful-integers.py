class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def valid_less_then(num): 
            n = len(num) - len(s)
            if n < 0:
                return 0 

            dp = [[0, 0] for _ in range(n + 1)]
            dp[-1][0] = 1
            dp[-1][1] = int(s <= num[n:])

            for i in range(n - 1, -1, -1): 
                dp[i][0] = (1 + limit) * dp[i + 1][0]
                if int(num[i]) <= limit:
                    dp[i][1] = int(num[i]) * dp[i + 1][0] + dp[i + 1][1]
                else:
                    dp[i][1] = dp[i][0]

            return dp[0][1]
        
        return valid_less_then(str(finish)) - valid_less_then(str(start-1))
        