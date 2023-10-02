class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #reference: https://www.youtube.com/watch?v=s_zu2dOkq80
        max_count = 0
        count = 0
        last_fruit = None
        second_last_fruit = None
        current_fruit_count = 0

        for fruit in fruits:
            if fruit == last_fruit or fruit == second_last_fruit:
                count += 1
            else:
                count = current_fruit_count + 1

            if fruit == last_fruit:
                current_fruit_count += 1
            else:
                current_fruit_count = 1

            if fruit != last_fruit:
                second_last_fruit = last_fruit
                last_fruit = fruit

            max_count = max(max_count, current_count)

        return max_count