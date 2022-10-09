class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuple_list = [(position[i],speed[i]) for i in range(len(position))]
        tuple_list.sort(key=lambda x: x[0], reverse=True)
        res = []
        for p, s in tuple_list:
            res.append((target - p) / s)
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()
        return len(res)