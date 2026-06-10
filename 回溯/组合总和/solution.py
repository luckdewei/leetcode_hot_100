from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """回溯 + 剪枝：O(n^(T/min)) 时间，O(T) 空间"""
        candidates.sort()
        res, path = [], []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                x = candidates[i]
                if x > remain:
                    break
                path.append(x)
                backtrack(i, remain - x)
                path.pop()

        backtrack(0, target)
        return res


# --- 本地测试 ---
if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 6, 7], 7))
