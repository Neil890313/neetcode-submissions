class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False]*len(nums)


        def backtrace():
            if len(path) == len(nums):
                res.append(path[:])
            
            for i in range(len(nums)):
                # add option
                if used[i] == True:
                    continue
                path.append(nums[i])
                used[i] = True
                # dfs
                backtrace()
                # remove
                path.pop()
                used[i] = False
        backtrace()

        return res
