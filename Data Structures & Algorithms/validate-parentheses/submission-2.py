class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 建立「右括號 -> 左括號」的對應表
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping: # 遇到右括號
                # 如果 stack 為空，給一個隨便的假值 '#' 讓它不匹配
                top_element = stack.pop() if stack else '#'
                
                # 如果彈出來的括號，跟字典裡記錄的正確配對不符
                if mapping[char] != top_element:
                    return False
            else:
                # 遇到左括號，直接推入 Stack
                stack.append(char)

        # 迴圈結束後，如果 Stack 被清空了，代表全數配對成功
        return not stack