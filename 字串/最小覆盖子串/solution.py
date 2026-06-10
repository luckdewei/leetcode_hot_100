from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """可变长滑动窗口：O(|s| + |t|) 时间"""
        if not t or not s:
            return ""

        need = Counter(t)
        window = Counter()
        required = len(need)
        formed = 0
        left = 0
        best_len = float("inf")
        best_left = 0

        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1

        return "" if best_len == float("inf") else s[best_left : best_left + best_len]


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))  # BANC
    print(s.minWindow("a", "a"))                # a
    print(s.minWindow("a", "aa"))               # ""
