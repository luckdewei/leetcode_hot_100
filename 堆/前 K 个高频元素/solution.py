from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """小根堆维护前 k 高频"""
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _, num in heap]


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)))  # [1, 2]
    print(s.topKFrequent([1], 1))  # [1]
