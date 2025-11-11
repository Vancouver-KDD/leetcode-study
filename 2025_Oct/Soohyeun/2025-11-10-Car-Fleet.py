class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        ans = 1
        while len(times) > 1:
            lead = times.pop()

            # if lead takes shorter -> separate group
            if lead < times[-1]:
                ans += 1
            # if lead takes longer -> fleet. reach to target at longer time
            else:
                times[-1] = lead

        return ans