from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """前缀和 + 哈希表：O(n) 时间，O(n) 空间"""
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num
            ans += prefix_count[prefix - k]
            prefix_count[prefix] += 1

        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1, 1, 1], 2))        # 2
    print(s.subarraySum([1, 2, 3], 3))        # 2
    print(s.subarraySum([1, -1, 0], 0))       # 3
