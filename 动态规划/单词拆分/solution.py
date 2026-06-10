from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))  # True
    print(s.wordBreak("applepenapple", ["apple", "pen"]))  # True
