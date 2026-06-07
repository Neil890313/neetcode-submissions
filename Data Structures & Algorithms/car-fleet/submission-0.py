class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(position)):
            time.append((target-position[i])/speed[i])
        pos_time = sorted(zip(position, time))

        count = 0
        max_num = 0
        for i in range(len(pos_time)-1, -1, -1):
            if pos_time[i][1] > max_num:
                max_num = pos_time[i][1]
                count += 1
        return count 