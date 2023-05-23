# https://peterdrinker.tistory.com/499

class SingleNumber:
    def find_single_number(self, nums: list[int]) -> int:
        result = 0
        for element in nums:
            result = element ^ result
        return result

def main():
    list = [3, 7, 4, 1, 7, 3, 2, 1, 2]
    single_number = SingleNumber()
    print(single_number.find_single_number(list))

if __name__ == '__main__':
    main()