from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """哈希分组：排序作为 key，O(n * k log k) 时间"""
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(sorted(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])))
    # [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]
    print(s.groupAnagrams([""]))       # [['']]
    print(s.groupAnagrams(["a"]))      # [['a']]
