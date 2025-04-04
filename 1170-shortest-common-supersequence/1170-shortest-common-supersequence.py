class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        n,m=len(s1),len(s2)
        dp=[[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        s=''
        i,j=n,m
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                s+= s1[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                s+=s1[i-1]
                i -= 1
            else:
                s+=s2[j-1]
                j -= 1
        while i>0:
            s+=s1[i-1]
            i-=1
        while j>0:
            s+=s2[j-1]
            j-=1   
        return s[-1::-1]