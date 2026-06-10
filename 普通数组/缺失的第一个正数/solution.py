from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """原地哈希：O(n) 时间，O(1) 空间"""
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))          # 3
    print(s.firstMissingPositive([3, 4, -1, 1]))      # 2
    print(s.firstMissingPositive([7, 8, 9, 11, 12]))  # 1
