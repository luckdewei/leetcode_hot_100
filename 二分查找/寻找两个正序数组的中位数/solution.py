from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """保证 nums1 较短，二分划分位置"""
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2  # nums1 左半取 i 个
            j = total_left - i  # nums2 左半取 j 个
            max_left1 = float("-inf") if i == 0 else nums1[i - 1]
            min_right1 = float("inf") if i == m else nums1[i]
            max_left2 = float("-inf") if j == 0 else nums2[j - 1]
            min_right2 = float("inf") if j == n else nums2[j]
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            elif max_left1 > min_right2:
                hi = i - 1
            else:
                lo = i + 1
        return 0.0


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))           # 2.0
    print(s.findMedianSortedArrays([1, 2], [3, 4]))       # 2.5
    print(s.findMedianSortedArrays([0, 0], [0, 0]))       # 0.0
