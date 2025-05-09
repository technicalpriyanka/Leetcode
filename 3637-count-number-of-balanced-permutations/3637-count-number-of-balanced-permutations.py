class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # 1. build digit counts and total sum
        mod = 10**9 + 7
        freq, total = [0] * 10, 0
        for ch in num:
            d = ord(ch) - ord('0')
            freq[d] += 1
            total += d
        n = len(num)
        even, odd = (n + 1) // 2, n // 2
        if total & 1: return 0

        # 2. precomp factorials & inv factorials upto n
        half, fact = total // 2, [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod
        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % mod

        # 3. DP over digits: dp[k][s] = sum of weights
        dp = [[0] * (half + 1) for _ in range(even + 1)]
        dp[0][0] = 1
        for d in range(10):
            c = freq[d]
            w = [invfact[e] * invfact[c - e] % mod for e in range(c + 1)]
            w0 = w[0]
            newdp = [[(dp[k][s] * w0) % mod for s in range(half + 1)]
                        for k in range(even+1)]
            for e in range(1, c + 1):
                dk, ds, we = e, d * e, w[e]
                if dk>even or ds>half:
                    break
                for k in range(even - dk, -1, -1):
                    row = dp[k]
                    tgt = newdp[k + dk]
                    lim = half - ds
                    for s in range(lim, -1, -1):
                        v = row[s]
                        if v:
                            tgt[s + ds] = (tgt[s + ds] + v * we) % mod
            dp = newdp
        
        weight_sum = dp[even][half]
        return (weight_sum * fact[even] * fact[odd]) % mod