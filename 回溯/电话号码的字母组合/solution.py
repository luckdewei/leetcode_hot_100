from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """回溯：O(3^n·4^m) 时间，O(n) 空间"""
        if not digits:
            return []
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        res, path = [], []

        def backtrack(i: int) -> None:
            if i == len(digits):
                res.append("".join(path))
                return
            for ch in mapping[digits[i]]:
                path.append(ch)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res


# --- 本地测试 ---
if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
