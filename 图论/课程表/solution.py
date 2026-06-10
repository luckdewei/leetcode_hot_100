from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """拓扑排序（Kahn BFS）：O(V+E) 时间，O(V+E) 空间"""
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        taken = 0
        while q:
            u = q.popleft()
            taken += 1
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return taken == numCourses


# --- 本地测试 ---
if __name__ == "__main__":
    print(Solution().canFinish(2, [[1, 0]]))       # True
    print(Solution().canFinish(2, [[1, 0], [0, 1]]))  # False
