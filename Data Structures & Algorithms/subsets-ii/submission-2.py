class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        path = []

        def backtrace(start):
            res.append(path[:])

            for i in range(start, len(nums)):
                # add option
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                # dfs(no reuse)
                backtrace(i+1)
                # remove option
                path.pop()
        backtrace(0)

        return res
