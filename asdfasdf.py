




8.10 - 8.35 

Given a string s, find the length of the longest substring without repeating characters.

Example 1: 

Input: s = "abcabcbb"

Output 3

The answer is abc, with the length of 3



Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


'''
Input: s = "abcabcbb"
l: explorere 
r: starting point

 
"a b c a b c b b"
   l
 r
 
"a b c a b c b b"
     l
 r
 
"a b c a b c b b"
       l
   r


'''

'''
" p w w k e w "
  l
    r
" p w w k e w "
  l
      r
" p w w k e w "
      l
      r
" p w w k e w "
      l
        r    

" p w w k e w "
      l
          r  
" p w w k e w "
        l
            r   
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        counter = 1
        
        if len(s) == 0:
          return 0
        
        for r in range(1,len(s)): # r = 1 # r = 2 
          while s[r] in s[l:r]: 
            # should include l and r characters    
              l += 1 # r = 1
          temp_counter = r - l + 1  # 1-0+1 = 2
          counter = max(temp_counter, counter) # 2 
        return counter 

        Input: s = "pwwkew"

O(n*m)
for i = 0 ; i < 0; i ++  < - outer loop
for j = 0 ; j < 0; i ++  < - inter  
O(N)

        
Inner Loop (While Loop): The inner while loop adjusts the left boundary of the sliding window (l) by moving it rightward until the substring s[l:r] does not contain the character s[r]. 
  This loop might seem to imply a nested iteration at first glance, 
  suggesting a quadratic time complexity. 
  However, the key to understanding its actual complexity lies in recognizing that each character is involved in at most two operations:

Being added to the current window when r advances.
Being removed from the current window when l advances.
        
        

    

    
    
8.46-9.15 
===========================================================================================================================================
'''
153. Find Minimum in Rotated Sorted Array
'''


Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Example 4:
Input: nums = [13,15,17,9]
Output: 9 
  
Example 1:
Input: nums = [4,5,0,1,2,3]
Output: 0 
  
O(log n)
# BST

# DFS
# BFS

# recursion


        
class Solution:
    def findMin(self, nums:List[int]):
        # find midst value
        
        # I will make condition 
       
        # I will call the function recursivelly 
       
        # 
       # [4,5,0,1,2,3]
       # 0 

       # [0,1,2,3,4,5]

       # [5,0,1,2,3,4]        
       # [3,4,5,0,1,2]


        
        
        
        
        
        
        
        
        