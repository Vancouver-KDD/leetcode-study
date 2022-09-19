//Input: nums = [1,2,3,4]  -> Output: [24,12,8,6]
//Input: nums = [-1,1,0,-3,3] -> Output: [0,0,9,0,0]

//Time Complexity: O(n), Space Complexity: O(1) (doesn't count of output array)

//my solution

class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return null;
        }
        
        int allNumProduct  = 1; // to save multiplication of all numbers
        int numOfZero = 0;
        
        for(int i = 0; i < nums.length ; i++){
            if(nums[i] == 0){ //In case of zero, just count the number of zero number
                numOfZero++;
            }else{ 
                allNumProduct *= nums[i]; 
            }            
        }
        
        int[] resultProduct = new int[nums.length];
        
        for(int i = 0; i < nums.length; i++){
            
            if(numOfZero > 1){
                resultProduct[i] = 0;
            }else if(numOfZero == 1){
                if(nums[i] == 0){
                    resultProduct[i] = allNumProduct;
                }else{
                    resultProduct[i] = 0; // because multiplying zero
                }
            }else{ // There is no zero number
                resultProduct[i] = allNumProduct / nums[i];
            }
        }
        
        return resultProduct;
        
    }
}


//Leetcode solution
//Input: nums = [1,2,3,4]  -> Output: [24,12,8,6]
//Input: nums = [-1,1,0,-3,3] -> Output: [0,0,9,0,0]
//Time Complexity: O(n), Space Complexity: O(1) (doesn't count of output array)
/*
class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return null;
        }
        
        int[] resultProductNum = new int[nums.length];
        
        int leftProductNum = 1;
        int rightProductNum = 1;
        
        //product leftSide numbers
        for(int i = 0; i < nums.length; i++){
            resultProductNum[i] = leftProductNum;
            leftProductNum *= nums[i];
        }
        
        //product both side numbers 
        for(int i = (nums.length-1) ; i >= 0; i--){
            resultProductNum[i] *= rightProductNum;
            rightProductNum *= nums[i];
        }
        
        return resultProductNum;
    }
}
*/