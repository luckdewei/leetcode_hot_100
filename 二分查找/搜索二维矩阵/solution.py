from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """将矩阵视为一维有序数组，二分查找"""
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(s.searchMatrix(mat, 3))   # True
    print(s.searchMatrix(mat, 13))  # False
