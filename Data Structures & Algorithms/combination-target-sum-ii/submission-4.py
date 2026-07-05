class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrace(start, remain):
            # 收集答案
            if remain == 0:
                res.append(path[:])
                return
            elif remain < 0:
                return
            
            for i in range(start, len(candidates)):
                # 增加選項
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                # dfs
                backtrace(i+1, remain-candidates[i])
                # 撤銷選項
                path.pop()

        backtrace(0, target)
        return res