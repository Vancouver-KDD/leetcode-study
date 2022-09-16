//intput: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  -> output : 6
//intput: nums = [-2, -1] -> output: -1


//Time complexity: O(n) , Space complexity: O(1)
//Dynamic Proframming, Kadane's Algorithm  ????? 
class Solution {
    
    public int maxSubArray(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return 0;
        }
        
        int largestSum = nums[0];
        int currentSum = nums[0];
        
        for(int i = 1; i < nums.length; i++){
            
            currentSum += nums[i];
            
            if(currentSum < nums[i]){ // reset sum
                currentSum = nums[i];
            }
            
            if(largestSum < currentSum){
                largestSum = currentSum;
            }
        }
        
        return largestSum;
        
    }
    
}
//using Divide & Cdonquer
// Time Complexity: O(nlogn), Space complexity:O(logn)
/*
class Solution {
    
    public int maxSubArray(int[] nums) {
        
        if(nums == null || nums.length < 1){
            return 0;
        }
        
        return recursiveMaxSubArray(nums, 0, nums.length-1);
    }
    
    int recursiveMaxSubArray(int[] nums, int start, int end){
        
        if(nums == null || nums.length < 1){
            return 0;
        }
        
       // System.out.println("["+start+","+end+"] ");
        
        if(start > end){
            return Integer.MIN_VALUE;
        }else if(start == end){
            return nums[start];
        }
        
        int mid = (start + end)/2;
        int leftMaxSum = 0;
        int rightMaxSum = 0;
        int currentSum = 0;
        
        //leftMax
        for(int i = (mid-1); i >= start; i--){
            currentSum += nums[i];
            leftMaxSum = Math.max(leftMaxSum, currentSum);
        }
        
        currentSum = 0;
        //Right maxSum
        for(int i = (mid+1); i <= end; i++){
            currentSum += nums[i];
            rightMaxSum = Math.max(rightMaxSum, currentSum);
        }
        
        int totalMaxSum = leftMaxSum + nums[mid] + rightMaxSum;
        
        //find max sum of left array
        int leftMaxSubArray = recursiveMaxSubArray(nums, start, mid-1);
        //find max sum of right array
        int rightMaxSubArray = recursiveMaxSubArray(nums, mid+1, end);
        
       // System.out.println("["+start+","+end+"] left:"+ leftMaxSubArray + ", right:"+rightMaxSubArray +", total:" + totalMaxSum);
        
        return Math.max(totalMaxSum, Math.max(leftMaxSubArray, rightMaxSubArray));        
        
    }
}
*/