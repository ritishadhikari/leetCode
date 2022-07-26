class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[-1] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j  # Need to insert `j` chars to become s2[:j]
                elif j == 0: 
                    dp[i][j] = i  # Need to delete `i` chars to become ""
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[m][n]

word1 = "horse"
word2 = "ros"

print(Solution().minDistance(s1=word1,s2=word2))