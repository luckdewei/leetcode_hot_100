from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """转置 + 每行反转：O(n^2) 时间，O(1) 空间"""
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(mat1)
    print(mat1)  # [[7,4,1],[8,5,2],[9,6,3]]

    mat2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(mat2)
    print(mat2)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
