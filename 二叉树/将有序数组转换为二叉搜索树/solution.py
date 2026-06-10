from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """分治递归：O(n) 时间，O(log n) 递归栈"""
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(nums) - 1)


def inorder(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# --- 本地测试 ---
if __name__ == "__main__":
    root = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    print(inorder(root))  # [-10, -3, 0, 5, 9]
