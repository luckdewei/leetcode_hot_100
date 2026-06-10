from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """回溯 + 记忆化回文判断：O(n·2^n) 时间，O(n^2) 空间"""
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        res, path = [], []

        def backtrack(start: int) -> None:
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if not is_pal[start][end]:
                    continue
                path.append(s[start : end + 1])
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return res


# --- 本地测试 ---
if __name__ == "__main__":
    print(Solution().partition("aab"))
