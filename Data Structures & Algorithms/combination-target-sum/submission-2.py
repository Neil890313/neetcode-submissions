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
                # add option
                path.append(nums[i])
                # dfs
                backtrace(i, remain - nums[i])
                # remove option
                path.pop()

        backtrace(0, target)
        return res