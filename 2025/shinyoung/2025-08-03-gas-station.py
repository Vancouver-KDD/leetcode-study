class Solution:
    def canCompleteCircuit(self, gas, cost):
        # Time: O(n)
        # Space: O(1)
        
        if sum(gas)<sum(cost):
            return -1
        
        start = total=0
        for i in range(len(gas)):
            total+=(gas[i]-cost[i])
            
            if total<0:
                total=0
                start=i+1
        
        return start
                


solution = Solution()
print(solution.canCompleteCircuit([1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(solution.canCompleteCircuit([2, 3, 4], cost=[3, 4, 3]))
