from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """单调递增栈 + 哨兵"""
        heights = [0] + heights + [0]
        stack = [0]  # 存下标，对应高度递增
        ans = 0
        for i in range(1, len(heights)):
            while heights[i] < heights[stack[-1]]:
                h_idx = stack.pop()
                h = heights[h_idx]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
    print(s.largestRectangleArea([2, 4]))               # 4
