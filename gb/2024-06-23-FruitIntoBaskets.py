class Solution:
    def totalFruit(self, fruits):
        if len(fruits) == 1:
            return len(fruits)
        fruitCount = collections.defaultdict(int)

        l = 0
        maxLen = 0
        for r in range(len(fruits)):
            currType = fruits[r]
            fruitCount[currType] += 1

            while len(fruitCount) > 2:
                fruitCount[fruits[l]] -= 1
                if fruitCount[fruits[l]] == 0:
                    del fruitCount[fruits[l]]

                l += 1

            maxLen = max(maxLen, (r - l + 1))
        return maxLen
