class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        offsets = [gas_val - cost_val for gas_val, cost_val in zip(gas, cost)]
        total, tank, start = 0, 0, 0
        for i in range(len(gas)):
            total += offsets[i]
            tank += offsets[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return start if total >= 0 else -1