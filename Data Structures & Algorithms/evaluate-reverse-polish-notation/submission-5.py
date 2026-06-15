class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        index = 0
        while index < len(tokens):
            print(stack)
            if tokens[index] not in ["+", "-", "*", "/"]:
                stack.append(tokens[index])
            else:
                operator = tokens[index]
                print(operator)
                val2 = int(stack.pop(-1))
                val1 = int(stack.pop(-1))
                if operator == "+":
                    new_val = val1 + val2
                if operator == "-":
                    new_val = val1 - val2
                if operator == "*":
                    new_val = val1 * val2
                if operator == "/":
                    new_val = int(val1 / val2) 
                stack.append(new_val)
            index += 1
        return int(stack[0])