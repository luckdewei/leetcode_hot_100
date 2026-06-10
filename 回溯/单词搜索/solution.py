from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """回溯 + DFS：O(mn·4^L) 时间，O(L) 空间"""
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int, k: int) -> bool:
            if k == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False
            tmp, board[r][c] = board[r][c], "#"
            found = (
                dfs(r + 1, c, k + 1)
                or dfs(r - 1, c, k + 1)
                or dfs(r, c + 1, k + 1)
                or dfs(r, c - 1, k + 1)
            )
            board[r][c] = tmp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


# --- 本地测试 ---
if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    print(Solution().exist([row[:] for row in board], "ABCCED"))  # True
