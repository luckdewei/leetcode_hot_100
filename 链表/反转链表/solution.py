from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """迭代反转：O(n) 时间，O(1) 空间"""
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


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
    print(list_to_vals(s.reverseList(build_list([1, 2, 3, 4, 5]))))  # [5,4,3,2,1]
    print(list_to_vals(s.reverseList(build_list([1, 2]))))             # [2,1]
    print(list_to_vals(s.reverseList(build_list([]))))                # []
