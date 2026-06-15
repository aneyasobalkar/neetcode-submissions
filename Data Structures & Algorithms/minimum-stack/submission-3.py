class MinStack:
    def __init__(self):
        self.min_stack = []
        self.main_stack = []
    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if self.min_stack and self.min_stack[-1] < val:
            val = self.min_stack[-1]
        self.min_stack.append(val)
    def pop(self) -> None:
        self.min_stack.pop()
        self.main_stack.pop()
    def top(self) -> int:
        if not self.main_stack:
            return
        return self.main_stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return
        return self.min_stack[-1]


