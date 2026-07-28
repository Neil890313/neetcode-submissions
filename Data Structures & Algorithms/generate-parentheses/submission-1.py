class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        

        def backtrace(left_count, right_count):
            if left_count == n and right_count == n:
                res.append(''.join(path))
            if left_count < n:
                path.append('(')
                backtrace(left_count+1, right_count)
                path.pop()
            if right_count < n and right_count < left_count:
                path.append(')')
                backtrace(left_count, right_count+1)
                path.pop()

        backtrace(0, 0)
        return res
