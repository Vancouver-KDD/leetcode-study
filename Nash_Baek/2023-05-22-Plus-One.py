class PlusOne:
    def plus_one(self, digits: list[int]) -> list[int]:
        string = str(int(''.join([str(element) for element in digits])) + 1)
        ret = []
        for s in string:
            ret.append(s)
        return ret

def main():
    plus_one = PlusOne()
    list = [9]
    print(plus_one.plus_one(list))

if __name__ == '__main__':
    main()