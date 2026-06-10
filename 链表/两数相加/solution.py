from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """模拟竖式加法：O(max(m,n)) 时间，O(1) 额外空间"""
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            carry, digit = divmod(s, 10)
            cur.next = ListNode(digit)
            cur = cur.next

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
    print(list_to_vals(s.addTwoNumbers(build_list([2, 4, 3]), build_list([5, 6, 4]))))  # [7,0,8]
    print(list_to_vals(s.addTwoNumbers(build_list([0]), build_list([0]))))             # [0]
    print(list_to_vals(s.addTwoNumbers(build_list([9, 9, 9, 9, 9, 9, 9]), build_list([9, 9, 9, 9]))))  # [8,9,9,9,0,0,0,1]
