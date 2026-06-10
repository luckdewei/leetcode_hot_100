from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """贪心：当前步数内能到的最远边界"""
        steps = 0
        cur_end = 0
        farthest = 0
        n = len(nums)
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                steps += 1
                cur_end = farthest
        return steps


if __name__ == "__main__":
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))  # 2
    print(s.jump([2, 3, 0, 1, 4]))  # 2
