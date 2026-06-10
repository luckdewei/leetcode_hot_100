from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        max_dp = min_dp = 1
        for x in nums:
            if x < 0:
                max_dp, min_dp = min_dp, max_dp
            max_dp = max(x, max_dp * x)
            min_dp = min(x, min_dp * x)
            ans = max(ans, max_dp)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))  # 6
    print(s.maxProduct([-2, 0, -1]))    # 0
