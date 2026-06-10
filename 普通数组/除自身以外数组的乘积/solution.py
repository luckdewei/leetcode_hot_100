from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """前缀积 + 后缀积：O(n) 时间，O(1) 额外空间（输出数组不计）"""
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))       # [24, 12, 8, 6]
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
