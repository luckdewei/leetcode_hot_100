from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]

if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))  # True
    print(s.canPartition([1, 2, 3, 5]))   # False
