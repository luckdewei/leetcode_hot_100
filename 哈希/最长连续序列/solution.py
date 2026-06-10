from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """哈希集合：只从序列起点扩展，O(n) 时间"""
        num_set = set(nums)
        ans = 0

        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                length = 1
                while cur + 1 in num_set:
                    cur += 1
                    length += 1
                ans = max(ans, length)

        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(s.longestConsecutive([]))  # 0
