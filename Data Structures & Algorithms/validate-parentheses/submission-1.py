class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                node = stack.pop()
                if char == ")" and node != "(" or char == "]" and node != "[" or char == "}" and node != "{":
                    return False

        return True if not stack else False