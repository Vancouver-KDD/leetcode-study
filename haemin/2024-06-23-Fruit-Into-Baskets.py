class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int) # mapping fruitType : countInBasket
        L, total, result = 0, 0, 0
        for R in range(len(fruits)):
            count[fruits[R]] += 1
            total += 1

            # check if the window is valid
            while len(count) > 2:
                f = fruits[L]
                count[f] -= 1
                total -= 1
                L += 1  # shrink the window till it's valid

                # in case count of the fruit is 0 - remove that key from our hashmap
                if not count[f]:
                    count.pop(f)

            result = max(result, total)

        return result