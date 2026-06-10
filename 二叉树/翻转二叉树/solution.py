from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """递归交换左右子树：O(n) 时间，O(h) 空间"""
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


def inorder(root: Optional[TreeNode]) -> list:
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# --- 本地测试 ---
if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inv = Solution().invertTree(root)
    print(inorder(inv))  # [6, 7, 4, 9, 2, 3, 1]（中序验证结构已翻转）
