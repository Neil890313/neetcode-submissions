class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrace(start, remain):
            if remain == 0:
                res.append(path[:])
                return
            elif remain < 0:
                return
            
            for i in range(start, len(candidates)):
                # 加入條件
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                # dfs
                backtrace(i+1, remain-candidates[i])
                # 撤銷條件
                path.pop()

        backtrace(0, target)
        return res