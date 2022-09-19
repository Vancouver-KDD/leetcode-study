// input : nums = [1, 2, 3, 1] , output : true
// input: nums = [1, 2, 3, 4], output: false
// Time complexity : O(n),   Space complexity : O(n)
class Solution {
    

    public boolean containsDuplicate(int[] nums) { 
        
        if(nums == null || nums.length == 0){
            return false; //error
        }
        
        HashSet<Integer> existedNum = new HashSet<Integer>();
        
        for(int i = 0; i < nums.length; i++){
            if(existedNum.contains(nums[i])){ //nums[i] is already existed.
                return true;
            }
            
            existedNum.add(nums[i]);  // nums[i] comes up for the first time.
        }
        
        return false; // There is no duplicated number
        
    }
    
}


