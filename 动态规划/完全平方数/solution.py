class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float("inf")] * n
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(12))  # 3
    print(s.numSquares(13))  # 2
