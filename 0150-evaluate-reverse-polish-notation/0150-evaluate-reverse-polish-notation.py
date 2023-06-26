class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # // integer division
        stack = []
        for token in tokens:
            if token == "+":
                num = stack.pop()
                num2 = stack.pop()
                stack.append(num + num2)
            elif token == "-":
                num = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num)
            elif token == "*":
                num = stack.pop()
                num2 = stack.pop()
                stack.append(num * num2)
            elif token == "/":
                num = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num))
            else:
                num = int(token)
                stack.append(num)
        return stack[-1]