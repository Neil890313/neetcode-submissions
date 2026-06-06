class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tmp = ['+', '-', '*', '/']
        stack = []
        for i in tokens:
            if i not in tmp:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                res = None
                if i == "+":
                    res = a+b
                elif i == "-":
                    res = b-a
                elif i == "*":
                    res = a*b
                else:
                    res = int(b / a)
                stack.append(res)
        return stack.pop()
        

