from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """单调递减双端队列：O(n) 时间"""
        dq = deque()
        ans = []

        for i, num in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)

            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # [3, 3, 5, 5, 6, 7]
    print(s.maxSlidingWindow([1], 1))  # [1]
