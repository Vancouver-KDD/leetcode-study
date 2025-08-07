class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0
        current_tank = 0
        start = 0

        for i in range(n):
            gain = gas[i] - cost[i]
            current_tank += gain
            total_tank += gain

            if current_tank < 0:
                current_tank = 0
                start = i + 1

        return start if total_tank >= 0 else -1
