class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[0] if m == 1 else dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))  # 28
    print(s.uniquePaths(3, 2))  # 3
