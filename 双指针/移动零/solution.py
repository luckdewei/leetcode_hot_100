from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """快慢指针：O(n) 时间，O(1) 空间，原地修改"""
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    a = [0, 1, 0, 3, 12]
    s.moveZeroes(a)
    print(a)  # [1, 3, 12, 0, 0]

    b = [0]
    s.moveZeroes(b)
    print(b)  # [0]
