from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """哈希表映射旧节点到新节点：O(n) 时间，O(n) 空间"""
        if not head:
            return None

        old_to_new = {None: None}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            old_to_new[cur].next = old_to_new[cur.next]
            old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]


def build_random_list(pairs):
    """pairs: [(val, random_index), ...], -1 表示 None"""
    if not pairs:
        return None
    nodes = [Node(v) for v, _ in pairs]
    for i, (_, r) in enumerate(pairs):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        nodes[i].random = nodes[r] if r >= 0 else None
    return nodes[0]


def random_list_to_pairs(head):
    if not head:
        return []
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    idx = {node: i for i, node in enumerate(nodes)}
    res = []
    for node in nodes:
        r = idx[node.random] if node.random else -1
        res.append((node.val, r))
    return res


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    head = build_random_list([(7, -1), (13, 0), (11, 4), (10, 1), (1, 0)])
    copied = s.copyRandomList(head)
    print(random_list_to_pairs(copied))  # 与输入结构相同
    print(random_list_to_pairs(s.copyRandomList(build_random_list([(3, -1), (3, 0), (3, -1)]))))
