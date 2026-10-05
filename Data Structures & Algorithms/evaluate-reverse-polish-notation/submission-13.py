class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                l,r = int(stack.pop()), int(stack.pop())
                stack.append(l+r)
            elif c == "*":
                l,r = int(stack.pop()), int(stack.pop())
                stack.append(l*r)
            elif c == "/":
                l,r = int(stack.pop()), int(stack.pop())
                stack.append(int(float(r)/l))
            elif c == "-":
                l,r = int(stack.pop()), int(stack.pop())
                stack.append(r-l)
            else:
                stack.append(c)
        return int(stack[0])