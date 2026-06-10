from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] <= amount else -1

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))  # 3
    print(s.coinChange([2], 3))         # -1
