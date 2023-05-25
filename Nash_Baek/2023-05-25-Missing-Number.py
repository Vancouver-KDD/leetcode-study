# https://peterdrinker.tistory.com/manage/posts/

class MissingNumber:
    def find_missing_number(self, nums: list[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result += i - nums[i]
        return result

def main():
    missing_number = MissingNumber()
    lst = [3, 0, 1]
    print(missing_number.find_missing_number(lst))

if __name__ == '__main__':
    main()