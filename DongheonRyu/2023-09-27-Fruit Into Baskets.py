# sliding window problem

def totalFruit(self, fruits: List[int]) -> int:
        hash_map = {}
        l, total, res = 0, 0, 0

        for i in fruits:
            hash_map[i] = hash_map.get(i, 0) + 1
            total += 1

            while len(hash_map) > 2:
                f = fruits[l]
                hash_map[f] -= 1
                if hash_map[f] == 0:
                    hash_map.pop(f)
                l += 1
                total -= 1

            res = max(res, total)
        return res