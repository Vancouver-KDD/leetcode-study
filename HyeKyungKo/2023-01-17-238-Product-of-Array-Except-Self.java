//input : nums = [1, 2, 3, 4]  -> output: [24, 12, 8, 6]
//input: nums = [-1,1,0,-3, 3] -> [0,0,9,0,0]
//2023-01-17
//[idea]
//first, save the product of all leftsides of current element
// nums = [1, 2, 3, 4]
//     [0] ->  [1]  ->  [2] ->  [3]
//left:   1,  1*1 = 1 , 1*2 = 2, 2*3 = 6
//second, update the product as the previous product * all rightside of elements.  
//        [3] ->  [2]  ->            [1]  ->             [0]
//prev: 1   ,  1*nums[3]=4    ,  prev*nums[2]=12  ,  prev*nums[1]=12*2=24
//      1*6=6, prev*left[2]=4*2=8, prev*left[1]=12*1=12, prev*left[0] = 24
// --> As a result, it is the product of all the elements of nums except nums[i]
// Time complexity : O(N)
// Space complexity: O(N)  
class Solution{
    public int[] productExceptSelf(int[] nums){
        if(nums == null || nums.length < 2){
            return new int[0]; //empty array
        }

        int[] productAll = new int[nums.length];
        //input: [-1,1,0,-3, 3] 
        int prev = 1;
        for(int i = 0; i < nums.length; i++){
            productAll[i] = prev; // save product of all leftsides
            prev *= nums[i];
        }
        //productAll = [1, -1, -1, 0, 0]
        prev = 1;
        for(int i = (nums.length-1); i >= 0; i--){
            productAll[i] *= prev; //left * right
            prev *= nums[i]; //start 1, then 3 -> -9 -> 0 -> 0
        }
        //updated productAll = [0*1, 0*3, -1*-9, -1*0, 1 *0]
        return productAll;
    }
}







//2022.11.29
//Time Complexity: O(N)
//Space Complexity: O(2*N)
/*
class Solution{
    public int[] productExceptSelf(int[] nums){
        if(nums == null || nums.length == 0){
            return null;
        }

        int[] leftProduct = new int[nums.length];
        int[] rightProduct = new int[nums.length];

        int value = 1;
        for(int i = 0 ; i < nums.length; i++){
            leftProduct[i] = value;
            value *= nums[i];
        }

        value = 1;
        for(int i = nums.length -1; i >= 0; i--){
            //rightProduct[i] = value;
            leftProduct[i] *= value;
            value *= nums[i];
        }

     
        //for(int i = 0; i < nums.length; i++){
        //    leftProduct[i] *= rightProduct[i];
       // }
        

        return leftProduct;
    }
}
*/
//Time Complexity: O(N)
//Space Complexty : O(N)
/*
class Solution{
    public int[] productExceptSelf(int[] nums){
        if(nums == null || nums.length == 0){
            return null;
        }

        int numOfZero = 0;
        int totalProduct = 1;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0){
                numOfZero++;
            }else{
                totalProduct *= nums[i];
            }
        }

        int[] product = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            if(numOfZero > 1){
                product[i] = 0;
            }else if(numOfZero == 1){
                if(nums[i] == 0){
                    product[i] = totalProduct;
                }else{
                    product[i] = 0;
                }
            }else{ // non zero value
                product[i] = totalProduct / nums[i];
            }
        }

        return product;
    }
}
*/
//2022.09.12
//Limitation : if nums is null or size is zero, return null

//Input: nums = [1,2,3,4]  -> Output: [24,12,8,6]
//Input: nums = [-1,1,0,-3,3] -> Output: [0,0,9,0,0]

//Time Complexity: O(n), Space Complexity: O(1) (doesn't count of output array)

//my solution
/*
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
*/

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