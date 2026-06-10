class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        start = max_len = 0

        def expand(l: int, r: int):
            nonlocal start, max_len
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            length = r - l - 1
            if length > max_len:
                max_len = length
                start = l + 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return s[start : start + max_len]

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))  # bab or aba
    print(s.longestPalindrome("cbbd"))   # bb
