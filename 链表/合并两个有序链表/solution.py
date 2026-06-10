from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """迭代合并：O(m + n) 时间，O(1) 空间"""
        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2
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
    print(list_to_vals(s.mergeTwoLists(build_list([1, 2, 4]), build_list([1, 3, 4]))))  # [1,1,3,4,4,4]
    print(list_to_vals(s.mergeTwoLists(None, None)))  # []
    print(list_to_vals(s.mergeTwoLists(None, build_list([0]))))  # [0]
