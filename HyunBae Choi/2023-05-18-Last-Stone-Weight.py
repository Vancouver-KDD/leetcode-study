# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Constraints:
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

# 1. we can use a max heap data structure
# 2. since Python does not have a max heap, we will use min heap and convert every number to negative
# 3. after popping the first 2 numbers, convert them to positive integers and "smash" them
# 4. if remainder is not 0, add back to the heap
# 5. repeat until theres either 1 or 0 stones left
# 6. append 0 incase heap is empty, else return the absolute value of the first index

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_largest  = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)

            if second_largest > first_largest:
                heapq.heappush(stones, first_largest - second_largest)

        stones.append(0)
        return abs(stones[0])