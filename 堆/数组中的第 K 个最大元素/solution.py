from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """小根堆维护 k 个最大元素：O(n log k)"""
        heap: List[int] = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
