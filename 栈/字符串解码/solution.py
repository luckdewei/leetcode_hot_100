class Solution:
    def decodeString(self, s: str) -> str:
        """栈：遇数字入栈倍数，遇 [ 入栈前缀，遇 ] 展开"""
        stack = []
        cur_num = 0
        cur_str = ""
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur_str, cur_num))
                cur_str, cur_num = "", 0
            elif ch == "]":
                prev_str, repeat = stack.pop()
                cur_str = prev_str + cur_str * repeat
            else:
                cur_str += ch
        return cur_str


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))       # aaabcbc
    print(s.decodeString("3[a2[c]]"))        # accaccacc
    print(s.decodeString("2[abc]3[cd]ef"))   # abcabccdcdcdef
