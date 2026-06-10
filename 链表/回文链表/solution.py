from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """找中点 + 反转后半 + 比较：O(n) 时间，O(1) 空间"""
        if not head or not head.next:
            return True

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = self._reverse(slow.next)
        slow.next = None

        p1, p2 = head, second
        ok = True
        while p2:
            if p1.val != p2.val:
                ok = False
                break
            p1 = p1.next
            p2 = p2.next

        slow.next = self._reverse(second)
        return ok

    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
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


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(build_list([1, 2, 2, 1])))  # True
    print(s.isPalindrome(build_list([1, 2])))        # False
