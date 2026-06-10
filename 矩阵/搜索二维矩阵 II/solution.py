from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """从右上角搜索：O(m + n) 时间，O(1) 空间"""
        if not matrix or not matrix[0]:
            return False

        row, col = 0, len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            if val > target:
                col -= 1
            else:
                row += 1

        return False


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    mat = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    print(s.searchMatrix(mat, 5))   # True
    print(s.searchMatrix(mat, 20))  # False
