from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """双指针切换链表：O(m + n) 时间，O(1) 空间"""
        pa, pb = headA, headB
        while pa is not pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    # listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], 交点 val=8
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)
    ha = ListNode(4)
    ha.next = ListNode(1)
    ha.next.next = common
    hb = ListNode(5)
    hb.next = ListNode(6)
    hb.next.next = ListNode(1)
    hb.next.next.next = common
    print(s.getIntersectionNode(ha, hb).val)  # 8
    print(s.getIntersectionNode(ha, ListNode(9)))  # None
