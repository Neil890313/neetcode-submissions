class Solution:
    def isPalidrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []

        def backtrace(start):
            if start == len(s):
                res.append(path[:])

            for i in range(start, len(s)):
                # add option
                substr = s[start:i+1]
                if not self.isPalidrome(substr):
                    continue
                path.append(substr)
                # dfs
                backtrace(i+1)
                # remove option
                path.pop()
        backtrace(0)
        return res 

