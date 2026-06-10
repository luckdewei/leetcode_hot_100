from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """迭代 + 栈：O(n) 时间，O(h) 空间"""
        res, stack = [], []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


# --- 本地测试 ---
if __name__ == "__main__":
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(Solution().inorderTraversal(root))  # [4, 2, 5, 1, 3]
    print(Solution().inorderTraversal(None))  # []
