class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []

        left_count = 0
        right_count = 0

        def backtrace(left_count, right_count):
            if left_count == n and right_count == n:
                res.append("".join(path))
            
            if left_count < n:
                # add option
                path.append('(')
                # dfs
                backtrace(left_count + 1, right_count)
                # remove option
                path.pop()
            if right_count < n and right_count < left_count:
                # add option
                path.append(')')
                # dfs
                backtrace(left_count, right_count + 1)
                # remove option
                path.pop()
        backtrace(0, 0)
        return res
