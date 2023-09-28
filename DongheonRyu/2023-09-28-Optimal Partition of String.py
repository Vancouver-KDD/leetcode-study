def partitionString(self, s: str) -> int:
        n_set = set()
        res = 1

        for i in s:
            if i in n_set:
                res += 1
                n_set = set()
                n_set.add(i)
            n_set.add(i)
        return res