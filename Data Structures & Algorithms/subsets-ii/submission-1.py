class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # [Important] sort
        nums.sort()

        path = []
        res = []

        def backtrace(start):
            res.append(path[:])

            for i in range(start, len(nums)):
                # [Important] condition add option
                if i > start and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                # dfs
                backtrace(i+1)
                # remove option
                path.pop()

        backtrace(0)
        return res