class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """滑动窗口 + 哈希表：O(n) 时间，O(min(n, |Σ|)) 空间"""
        last = {}
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            ans = max(ans, right - left + 1)

        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring("bbbbb"))      # 1
    print(s.lengthOfLongestSubstring("pwwkew"))     # 3
