from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """快慢指针 + 哑节点：O(L) 时间，O(1) 空间"""
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


def build_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def list_to_vals(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(list_to_vals(s.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 2)))  # [1,2,3,5]
    print(list_to_vals(s.removeNthFromEnd(build_list([1]), 1)))               # []
    print(list_to_vals(s.removeNthFromEnd(build_list([1, 2]), 1)))            # [1]
