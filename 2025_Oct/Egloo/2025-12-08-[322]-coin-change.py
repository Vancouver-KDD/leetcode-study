class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = {}
        if amount == 0:
            return 0

        def change(amt):
            if amt in coins:
                return 1
            else:
                if amt in cache:
                    return cache[amt]

                t_min = float('inf')
                for c in coins:
                    if amt - c < 0:
                        continue 
                    r = change(amt - c)
                    if r != -1:
                        if change(amt - c) < t_min:
                            t_min = change(amt - c)
                
                if t_min == float('inf'):
                    cache[amt] = -1
                else:
                    cache[amt] = t_min + 1

                return cache[amt]
                
        return change(amount)