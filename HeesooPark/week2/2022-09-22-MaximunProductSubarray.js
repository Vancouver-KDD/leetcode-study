// Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

// The test cases are generated so that the answer will fit in a 32-bit integer.

// A subarray is a contiguous subsequence of the array.



// Example 1:

// Input: nums = [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.
// Example 2:

// Input: nums = [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


// Constraints:

// 1 <= nums.length <= 2 * 104
// -10 <= nums[i] <= 10
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


// when elements are all positive
// [1,2,3,4] -> Max will be always when prevMax * curElement

// when elements are all negative
// [-1, -2, -3, -4] -> -1, 2, -6, 24 -> -6 was the Min but when the negative multiplied, it turned into Max.

// We can think that we need to keep track of Min until the current element.
// [2,3,-2, 0, 4,-1]
// 2, 6, -12, -48, 48
// 3/ -6/ -24/ 24
// store the current Max, Min value and previous product

const maxProduct = (nums) => {

    if (nums.length === 0) return 0;

    let preMax = nums[0];
    let preMin = nums[0];
    let max = nums[0];

    // if we don't have preMax, preMin separately, inside for loop, it will use updated curMax to calculate curMin
    let curMax = 1;
    let curMin = 1;

    for(let i = 1; i < nums.length; i++) {
        curMax = Math.max(preMax * nums[i], nums[i], preMin * nums[i]);

        curMin = Math.min(preMax * nums[i], nums[i], preMin * nums[i]);

        // need to set curMax, curMin as preMax, preMin
        preMax = curMax;
        preMin = curMin;

        max = Math.max(max, curMax);

    }

    return max;

}

