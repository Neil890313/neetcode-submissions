class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(substr):
            l = 0
            r = len(substr)-1
            while l <= r:
                if substr[l] != substr[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrace(start):
            # 收集path
            if start == len(s):
                res.append(path[:])

            for i in range(start, len(s)):
                # 增加選項
                substr = s[start:i+1]
                if not isPalindrome(substr):
                    continue
                path.append(substr)
                # dfs
                backtrace(i+1)
                # 撤銷選項
                path.pop()
        
        backtrace(0)
        return res