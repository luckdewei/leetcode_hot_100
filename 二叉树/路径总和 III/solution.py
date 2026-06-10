from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """前缀和 + 哈希表：O(n) 时间，O(n) 空间"""
        self.ans = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node: Optional[TreeNode], cur: int) -> None:
            if not node:
                return
            cur += node.val
            self.ans += prefix[cur - targetSum]
            prefix[cur] += 1
            dfs(node.left, cur)
            dfs(node.right, cur)
            prefix[cur] -= 1

        dfs(root, 0)
        return self.ans


# --- 本地测试 ---
if __name__ == "__main__":
    root = TreeNode(10,
                    TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
                    TreeNode(-3, None, TreeNode(11)))
    print(Solution().pathSum(root, 8))  # 3
