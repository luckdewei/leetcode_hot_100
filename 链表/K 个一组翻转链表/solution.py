from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """分组反转：O(n) 时间，O(1) 空间"""
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self._get_kth(group_prev, k)
            if not kth:
                break

            group_next = kth.next
            prev, cur = kth.next, group_prev.next

            while cur is not group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def _get_kth(self, cur: ListNode, k: int) -> Optional[ListNode]:
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur


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
    print(list_to_vals(s.reverseKGroup(build_list([1, 2, 3, 4, 5]), 2)))  # [2,1,4,3,5]
    print(list_to_vals(s.reverseKGroup(build_list([1, 2, 3, 4, 5]), 3)))  # [3,2,1,4,5]
