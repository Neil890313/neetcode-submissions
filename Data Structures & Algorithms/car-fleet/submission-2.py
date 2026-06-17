class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for p, s in zip(position, speed):
            time.append((target-p)/s)
        p_t_list = sorted(zip(position, time))

        max_num = 0
        fleet = 0

        for i in range(len(p_t_list)-1, -1, -1):
            if p_t_list[i][1] > max_num:
                max_num = p_t_list[i][1]
                fleet += 1
        return fleet