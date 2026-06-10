from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = prev1 = 0
        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1

if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2, 3, 1]))      # 4
    print(s.rob([2, 7, 9, 3, 1]))   # 12
