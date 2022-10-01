/**
 * Given an integer array nums, return true if any value appears at least twice in the array, 
 * and return false if every element is distinct.
 * Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
 */

// first solution
var containsDuplicate = function(nums) {
    let map = {};
    
    for(let i=0; i<nums.length; i++){
        // if map has no same key, add new key and val
        if(!map.hasOwnProperty(nums[i])){
            map[nums[i]] = i;    
        } else {
            // if map has same key
            return true    
        }
    }
    // if no duplicates, return false
    return false
};

// second solution
var containsDuplicate = function(nums) {
    let numSet = new Set(nums);
    
    // if length is not identical, return true
    return nums.length === numSet.size ? false : true
};