from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """一次遍历：维护最低买入价"""
        min_price = float("inf")
        ans = 0
        for p in prices:
            min_price = min(min_price, p)
            ans = max(ans, p - min_price)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(s.maxProfit([7, 6, 4, 3, 1]))     # 0
