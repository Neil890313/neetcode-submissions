class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[i]:
                tmp = s.pop()
                ans[tmp] = i-tmp
            s.append(i)
        return ans 