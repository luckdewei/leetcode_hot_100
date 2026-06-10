from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """二分查找旋转数组"""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 左半段有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右半段有序
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(s.search([1], 0))                     # -1
