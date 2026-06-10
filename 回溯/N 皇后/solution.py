from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """回溯 + 列/对角线冲突检测：O(n!) 时间，O(n^2) 空间"""
        res, board = [], ["." * n for _ in range(n)]
        cols, diag1, diag2 = set(), set(), set()

        def backtrack(row: int) -> None:
            if row == n:
                res.append(board[:])
                return
            for col in range(n):
                d1, d2 = row - col, row + col
                if col in cols or d1 in diag1 or d2 in diag2:
                    continue
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)
                board[row] = "." * col + "Q" + "." * (n - col - 1)
                backtrack(row + 1)
                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)

        backtrack(0)
        return res


# --- 本地测试 ---
if __name__ == "__main__":
    print(Solution().solveNQueens(4))
