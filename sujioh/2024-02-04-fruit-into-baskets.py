class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        l, sub_len, res = 0, 0, 0

        for r in range(len(fruits)):
            type_r = fruits[r]
            count[type_r] = count.get(type_r, 0) + 1
            total += 1

            while len(count) > 2:
                type_l = fruits[l]
                count[type_l] -= 1
                sub_len -= 1
                l += 1
                if count[type_l] == 0:
                    del count[type_l]
            res = max(res, sub_len)

        return res