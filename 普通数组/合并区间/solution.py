from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """排序后合并：O(n log n) 时间，O(1) 额外空间（不含排序）"""
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        return merged


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
    print(s.merge([[1, 4], [4, 5]]))                     # [[1,5]]
    print(s.merge([[1, 4], [0, 4]]))                     # [[0,4]]
