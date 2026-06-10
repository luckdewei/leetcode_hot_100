from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """中序遍历 + 递增检查：O(n) 时间，O(h) 空间"""
        self.prev = float("-inf")

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            if not dfs(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return dfs(node.right)

        return dfs(root)


# --- 本地测试 ---
if __name__ == "__main__":
    valid = TreeNode(2, TreeNode(1), TreeNode(3))
    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(Solution().isValidBST(valid))    # True
    print(Solution().isValidBST(invalid))  # False
