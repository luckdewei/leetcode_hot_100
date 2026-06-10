from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """回溯，控制左右括号数量：O(4^n/√n) 时间，O(n) 空间"""
        res, path = [], []

        def backtrack(open_cnt: int, close_cnt: int) -> None:
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if open_cnt < n:
                path.append("(")
                backtrack(open_cnt + 1, close_cnt)
                path.pop()
            if close_cnt < open_cnt:
                path.append(")")
                backtrack(open_cnt, close_cnt + 1)
                path.pop()

        backtrack(0, 0)
        return res


# --- 本地测试 ---
if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
