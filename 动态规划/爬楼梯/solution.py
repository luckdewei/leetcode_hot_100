class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))  # 2
    print(s.climbStairs(3))  # 3
