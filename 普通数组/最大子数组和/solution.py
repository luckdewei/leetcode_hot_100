from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Kadane 算法：O(n) 时间，O(1) 空间"""
        cur = ans = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            ans = max(ans, cur)
        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(s.maxSubArray([1]))                               # 1
    print(s.maxSubArray([5, 4, -1, 7, 8]))                  # 23
