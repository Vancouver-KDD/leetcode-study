class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        basket = {} # contains with fruits we put. key as fruit type, value as # of fruit
        max_num_fruit = 0

        for right, fruit in enumerate(fruits):
            # Put the fruit right pointer is pointing in basket
            basket[fruit] = 1 if fruit not in basket else basket[fruit] + 1

            # Move left pointer to the right until basket only contains less than or equal to 2 fruits
            while len(basket) > 2:
                the_most_left_fruit = fruit[left]
                basket[the_most_left_fruit] -= 1
                if basket[the_most_left_fruit] == 0:
                    basket.pop(the_most_left_fruit)
                left += 1

            # Find maximum number of fruits we can put so far
            max_num_fruit = max(max_num_fruit, sum(basket.values()))

            return max_num_fruit
