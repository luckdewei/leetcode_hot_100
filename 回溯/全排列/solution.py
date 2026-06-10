from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """回溯 + used 数组：O(n·n!) 时间，O(n) 空间"""
        res, path, used = [], [], [False] * len(nums)

        def backtrack() -> None:
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res


# --- 本地测试 ---
if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
