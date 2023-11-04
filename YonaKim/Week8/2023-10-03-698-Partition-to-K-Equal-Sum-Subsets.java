import java.util.Arrays;

/**
* Time Complexity: O(n)
* Space Complexity: O(k) created extra data structure int[] bucket of size k.
*/
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        //we can't partition nums of size < k into k partitions
        if(nums.length < k) {
            return false;
        }

        int totalSum=0;
        //compute total sum of nums array
        for(int n : nums) {
            totalSum += n;
        }
        
        //totalSum % k must be dividable by k
        if(totalSum % k != 0) return false;
        
        //sort nums. We'll start from taking the last element
        Arrays.sort(nums);
        
        //our target is sum/k and we have to find this in nums, k times then it is valid
        return helper(nums, totalSum / k, nums.length - 1, new int[k]);
    }

    public boolean helper(int[] arr, int targetSum, int i, int[] bucket){
        
        //we have gone through all elements of arr
        if(i == -1) {
            return true;
        }
        
        //start filling the bucket array
        for(int j = 0; j < bucket.length; j++) {
            
            //can we take this ith element
            if(bucket[j] + arr[i] <= targetSum) {
            
                //if we take this element
                bucket[j] += arr[i];
                
                //go to next element (in our case we go to the smallest element because we are sorted)
                //if we can fill all buckets then return true
                if(helper(arr, targetSum, i-1, bucket))
                    return true;
                
                //we can't fill another bucket if we take the ith element. Don't fill the bucket with this element
                bucket[j]-=arr[i];
            
            }
            
            //if our bucket is empty means we have not taken any elements in the buckets
            if(bucket[j]==0)
                break;
        
        }
        
        //all buckets are full but i is pointing to some element (elements still left)
        //or our bucket is empty means we haven't take any element (not valid)
        return false;
    
    }
}