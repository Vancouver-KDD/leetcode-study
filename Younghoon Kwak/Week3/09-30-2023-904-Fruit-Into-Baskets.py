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
    

    aaaa(c)bb(c)aab k = 3;
'aaaa' 2 conditions c



# Create Dictionary 
# Save all the occurences of the chracters by looping through the given string
# { "a": 2 }

# Loop through this dictionary with the key / values 
# First have to check occurence is more than k. chracters that are less than 'k'
# Once found a character that is less than 'k'
# Split the given string with the chracter that is less than k. 

s: str, k: int 


char_dict = {}

k = 3, aabbcc


{a: 1, b: 2}
for character in s:
	if chracter is in char_dict.keys():
  		count =  char_dict[character]
      char_dict[chracter] = count + 1
    else:
    	char_dict[charcter] = 1

    #keys      #count
for character, occurence in char_dict.items():
				
      if occurence is less than k:
      
      		return max(logestSubsring(sub_string, k) for sub_string in s.split(chracter))
          aabb
          # aaacbb k = 2
          aaa bb
  if len(s) < k 
  	reutrn 0
    
  return len(s)