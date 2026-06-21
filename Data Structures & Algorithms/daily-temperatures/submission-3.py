class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        s = []

        for i in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[i]:
                node = s.pop()
                ans[node] = i - node
            s.append(i)
        
        return ans