/*
 * https://leetcode.com/problems/boats-to-save-people/description/
 * 
 * ## Description

    You are given an array `people` where `people[i]` is the weight of the `ith` person, and an **infinite number of boats where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most.

    Return the minimum number of boats to carry every given person.
 *
 * ## Intuition 
 * 
 *  To send the minimum number of boats, the most ideal way is sending each boat with the weight reaching as close to the limit as possible
 *  because each boat can carry only two people at the same time and we would like to make the most out of it. ⇒ Greedy solution 
 *  
 *  Better to get the heaviest person first because we could see if we can pair with the least heaviest person.
 *  if not, we send the heaviest person by a separate boat, and look for the second heaviest person and check if we can pair with the least heaviest        *  person. . . and continue the process. ⇒ Two pointers solution
 */

import java.util.Arrays;

class Solution {
    public int numRescueBoats(int[] people, int limit) {
        //Sort the array to identify the heaviest and the lightest person. 
        Arrays.sort(people);
        
        //number of boats required 
        int boats = 0; 

        //Initialize the left and right pointer to the both ends of array 
        int left = 0, right = people.length - 1; 

        //Traverse until left pointer and right pointer has met => if not, that means there is still a person to save! 
        while(left <= right) {
            //Check if the sum of the two people from both ends exceeds limit
            if(people[left] + people[right] > limit) {
                //If so, only take the heavier person to a single boat, and move the right pointer to the next heaviest person. 
                right--; 
            } else {
                //If not, a boat can carry the pair at the same time, then move the both pointers.  
                left++; 
                right--; 
            }

            boats++; // count the boat 
        }

        return boats;
    }
}