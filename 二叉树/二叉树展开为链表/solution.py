from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """后序遍历收集节点，再串联：O(n) 时间，O(n) 空间"""
        nodes = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            nodes.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        for i in range(len(nodes) - 1):
            nodes[i].right = nodes[i + 1]
            nodes[i].left = None
        if nodes:
            nodes[-1].left = None
            nodes[-1].right = None


def to_list(root: Optional[TreeNode]) -> list:
    res = []
    while root:
        res.append(root.val)
        root = root.right
    return res


# --- 本地测试 ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    Solution().flatten(root)
    print(to_list(root))  # [1, 2, 3, 4, 5, 6]
