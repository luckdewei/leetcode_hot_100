from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """递归 + 哈希表定位根：O(n) 时间，O(n) 空间"""
        idx = {v: i for i, v in enumerate(inorder)}

        def build(pre_lo: int, pre_hi: int, in_lo: int, in_hi: int) -> Optional[TreeNode]:
            if pre_lo > pre_hi:
                return None
            root_val = preorder[pre_lo]
            mid = idx[root_val]
            left_size = mid - in_lo
            root = TreeNode(root_val)
            root.left = build(pre_lo + 1, pre_lo + left_size, in_lo, mid - 1)
            root.right = build(pre_lo + left_size + 1, pre_hi, mid + 1, in_hi)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)


def inorder(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# --- 本地测试 ---
if __name__ == "__main__":
    root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(inorder(root))  # [9, 3, 15, 20, 7]
