from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Floyd 快慢指针：O(n) 时间，O(1) 空间"""
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


def build_cycle_list(vals, pos):
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.hasCycle(build_cycle_list([3, 2, 0, -4], 1)))  # True
    print(s.hasCycle(build_cycle_list([1, 2], 0)))           # True
    print(s.hasCycle(build_cycle_list([1], -1)))             # False
