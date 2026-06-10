from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """后序 DFS 计算深度并更新直径：O(n) 时间，O(h) 空间"""
        self.ans = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.ans


# --- 本地测试 ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(Solution().diameterOfBinaryTree(root))  # 3（路径 4-2-5 或 5-2-4）
