class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while len(stones) > 1:
            stones.sort(reverse=True)
            x = stones[0]
            y = stones[1]

            if x > y:
                temp = x
                x = y
                y = temp

            if x == y:
                stones.remove(x)
                stones.remove(y)
            else:
                diff = y - x
                stones.remove(x)
                stones.remove(y)
                stones.append(diff)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0
