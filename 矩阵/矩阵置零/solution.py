from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """用首行首列作标记：O(mn) 时间，O(1) 空间"""
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    mat1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(mat1)
    print(mat1)  # [[1,0,1],[0,0,0],[1,0,1]]

    mat2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 0, 5]]
    s.setZeroes(mat2)
    print(mat2)  # [[0,0,0,0],[0,4,5,0],[0,3,0,0]]
