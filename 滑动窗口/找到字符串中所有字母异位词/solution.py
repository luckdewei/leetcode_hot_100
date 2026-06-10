from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """定长滑动窗口 + 频次比较：O(n) 时间"""
        if len(p) > len(s):
            return []

        need = Counter(p)
        window = Counter()
        ans = []
        k = len(p)

        for right, ch in enumerate(s):
            window[ch] += 1

            left = right - k + 1
            if left < 0:
                continue

            if window == need:
                ans.append(left)

            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]

        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
    print(s.findAnagrams("abab", "ab"))         # [0, 1, 2]
