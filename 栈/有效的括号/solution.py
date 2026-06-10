class Solution:
    def isValid(self, s: str) -> bool:
        """栈匹配括号"""
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))       # True
    print(s.isValid("()[]{}"))   # True
    print(s.isValid("(]"))       # False
    print(s.isValid("([)]"))     # False
