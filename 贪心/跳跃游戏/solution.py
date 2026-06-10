from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """维护最远可达位置"""
        reach = 0
        for i, jump in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + jump)
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))  # True
    print(s.canJump([3, 2, 1, 0, 4]))  # False
