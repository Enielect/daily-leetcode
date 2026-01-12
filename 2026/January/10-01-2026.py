class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        # dp[i][j] = min ASCII delete sum to make s1[0:i] and s2[0:j] equal
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: delete all characters from s1 (when s2 is empty)
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        # Base case: delete all characters from s2 (when s1 is empty)
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    # Characters match, no deletion needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Delete from s1 or s2, take minimum cost
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),  # delete s1[i-1]
                        dp[i][j - 1] + ord(s2[j - 1]),  # delete s2[j-1]
                    )

        return dp[m][n]


print(Solution().minimumDeleteSum("sea", "eat"))
