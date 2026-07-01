class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrace(left_count, right_count):
            # 加入 res 的 條件?
            if left_count == n and right_count == n:
                res.append("".join(path))
                return
            if left_count < n:
                path.append("(")
                backtrace(left_count+1, right_count)
                path.pop()
            if right_count < n and right_count < left_count:
                path.append(")")
                backtrace(left_count, right_count+1)
                path.pop()

        backtrace(0, 0)
        return res