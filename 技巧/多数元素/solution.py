from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Boyer-Moore 投票"""
        cand = count = 0
        for x in nums:
            if count == 0:
                cand = x
            count += 1 if x == cand else -1
        return cand

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))           # 3
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
