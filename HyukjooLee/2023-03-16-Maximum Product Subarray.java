// Given an integer array nums, find a 
// subarray that has the largest product, and return the product.

// The test cases are generated so that the answer will fit in a 32-bit integer.

// Input: nums = [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.


// using dp to find the subarray that has the largest product
// time complexity is O(N); the length of the input array
// space complexity is O(1); to store maxProd, minProd, overallMaxProd
public int maxProduct(int[] nums) {
    int n = nums.length;
    
    // maximum and minimum product
    int maxProd = nums[0];
    int minProd = nums[0];
    
    // to keep track of the overall maximum product
    int overallMaxProd = nums[0];
    
    for (int i = 1; i < n; i++) {
        // we swap the maxProd and minProd variables if the current element is negative value 
        if (nums[i] < 0) {
            int temp = maxProd;
            maxProd = minProd;
            minProd = temp;
        }
        
        // update the maxProd and minProd based on the current element
        maxProd = Math.max(nums[i], maxProd * nums[i]);
        minProd = Math.min(nums[i], minProd * nums[i]);

        overallMaxProd = Math.max(overallMaxProd, maxProd);
    }
    
    return overallMaxProd;
}
