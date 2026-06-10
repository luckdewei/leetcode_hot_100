from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """三次反转：O(n) 时间，O(1) 空间"""
        n = len(nums)
        k %= n
        if k == 0:
            return

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums1, 3)
    print(nums1)  # [5, 6, 7, 1, 2, 3, 4]

    nums2 = [-1, -100, 3, 99]
    s.rotate(nums2, 2)
    print(nums2)  # [3, 99, -1, -100]
