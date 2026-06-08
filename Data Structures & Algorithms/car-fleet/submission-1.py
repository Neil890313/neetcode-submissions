class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target-pos)/sped for pos, sped in zip(position, speed)]
        pos_time = sorted(zip(position, time))
        max_time = 0
        count = 0

        for i in range(len(pos_time)-1, -1, -1):
            if pos_time[i][1] > max_time:
                max_time = pos_time[i][1] 
                count += 1
        return count