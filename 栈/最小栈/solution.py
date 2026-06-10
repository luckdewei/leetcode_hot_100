class MinStack:
    """每个元素 paired 存当前最小值"""

    def __init__(self):
        self.stack = []  # (value, current_min)

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# --- 本地测试 ---
if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())  # -3
    ms.pop()
    print(ms.top())     # 0
    print(ms.getMin())  # -2
