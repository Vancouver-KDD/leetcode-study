class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        window_start = 0 # store window starting index
        basket = {}     # store fruits
        max_no_of_fruits = -float('inf')  # store maximum no of fruits
        
        for window_end in range(len(fruits)): # iterate over all the fruits
            right_fruit = fruits[window_end]  # take out right fruit
            # store fruit in the basket
            if right_fruit not in basket:
                basket[right_fruit] = 0
            basket[right_fruit] +=1

            
            # shrink the window until basket contain more than 2 distinct fruits
            while len(basket) > 2:
                left_fruit = fruits[window_start]  # take out left fruit
                basket[left_fruit] -=1 # remove it from the basket
				
				# if the count of left fruit is zero then delete it from the basket 
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                   
		
                window_start += 1   # shrink the window  

            curr_no_of_fruits = window_end - window_start  + 1 # find current no of fruits in the basket 
            max_no_of_fruits = max(max_no_of_fruits,curr_no_of_fruits) #update max_no_of_fruits if current no of fruits is greater than maximum no of fruits
            
        return max_no_of_fruits