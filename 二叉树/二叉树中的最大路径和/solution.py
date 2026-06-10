from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """后序 DFS，维护全局最大路径和：O(n) 时间，O(h) 空间"""
        self.ans = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return self.ans


# --- 本地测试 ---
if __name__ == "__main__":
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().maxPathSum(root))  # 42
