from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """回溯枚举子集：O(n·2^n) 时间，O(n) 空间"""
        res, path = [], []

        def backtrack(start: int) -> None:
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res


# --- 本地测试 ---
if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
