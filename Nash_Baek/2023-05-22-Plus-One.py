class PlusOne:
    def plus_one(self, digits: list[int]) -> list[int]:
        string = str(int(''.join([str(element) for element in digits])) + 1)
        ret = []
        for s in string:
            ret.append(s)
        return ret

plus_one = PlusOne()
list = [9]
print(plus_one.plus_one(list))