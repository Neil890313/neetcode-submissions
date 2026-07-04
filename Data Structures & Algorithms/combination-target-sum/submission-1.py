class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrace(start, remain):
            if remain == 0:
                res.append(path[:])
                return
            elif remain < 0:
                return
            
            for i in range(start, len(nums)):
                # 增加選項
                path.append(nums[i])
                # dfs
                backtrace(i, remain-nums[i])
                # 撤銷選項
                path.pop()

        backtrace(0, target)
        return res