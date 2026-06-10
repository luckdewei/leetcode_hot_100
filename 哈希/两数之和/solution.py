from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """哈希表解法：O(n) 时间，O(n) 空间"""
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        return []


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(s.twoSum([3, 2, 4], 6))         # [1, 2]
    print(s.twoSum([3, 3], 6))           # [0, 1]
