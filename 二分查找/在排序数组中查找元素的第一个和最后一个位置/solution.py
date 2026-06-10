from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """两次二分：左边界 + 右边界"""

        def lower_bound(x: int) -> int:
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def upper_bound(x: int) -> int:
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        left = lower_bound(target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, upper_bound(target) - 1]


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
    print(s.searchRange([], 0))                   # [-1, -1]
