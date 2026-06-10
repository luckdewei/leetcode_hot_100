from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """递归后序：O(n) 时间，O(h) 空间"""
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


# --- 本地测试 ---
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                    TreeNode(1, TreeNode(0), TreeNode(8)))
    p, q = root.left, root.right
    lca = Solution().lowestCommonAncestor(root, p, q)
    print(lca.val)  # 3
