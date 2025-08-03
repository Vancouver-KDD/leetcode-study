# KDD LeetCode Study Week 9: Greedy
# Assignment 1
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/gas-station

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        if total_gas < total_cost:
            return -1
        
        current_tank = 0
        start_station = 0
        
        for i in range(n):
            current_tank += gas[i] - cost[i]
            
            if current_tank < 0:
                start_station = i + 1
                current_tank = 0
        
        return start_station
