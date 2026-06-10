from collections import OrderedDict


class LRUCache:
    """OrderedDict：get/put 均摊 O(1)"""

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


# --- 本地测试 ---
if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))    # 1
    lru.put(3, 3)        # 淘汰 key 2
    print(lru.get(2))    # -1
    lru.put(4, 4)        # 淘汰 key 1
    print(lru.get(1))    # -1
    print(lru.get(3))    # 3
    print(lru.get(4))    # 4
