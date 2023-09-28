class Solution:
    '''
    sliding window template
    - always move right first

    lo, hi = 0, 0
    while hi < len(input):
        # do something (usually if statement)
        # right += 1

        # do something (usually either if or while statement)
        # left += 1


    time: O(n) # left and right pointer moves at most n times, where n in length of fruits
    space: O(1) dictionary contains at most 3 fruits at once.
    '''

    def totalFruit(self, fruits: List[int]) -> int:

        dict = defaultdict(int)  # basket
        k = 2  # number of fruit type supported

        left, right = 0, 0
        max_fruits = 0

        while right < len(fruits):

            right_fruit = fruits[right]
            dict[right_fruit] += 1

            if len(dict) <= k:
                max_fruits = max(max_fruits, right - left + 1)

            right += 1

            while len(dict) > k:
                left_fruit = fruits[left]
                dict[left_fruit] -= 1
                if dict[left_fruit] == 0:
                    del dict[left_fruit]
                left += 1

        return max_fruits