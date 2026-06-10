from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """双指针解法：O(n) 时间，O(1) 空间"""
        left, right = 0, len(height) - 1
        ans = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            ans = max(ans, h * w)

            # 移动较短的一侧，才有机会让「短板」变高
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(s.maxArea([1, 1]))                         # 1
