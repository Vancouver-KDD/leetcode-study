// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.



// Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation:
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.
// Example 2:

// Input: nums = [0,1,1]
// Output: []
// Explanation: The only possible triplet does not sum up to 0.
// Example 3:

// Input: nums = [0,0,0]
// Output: [[0,0,0]]
// Explanation: The only possible triplet sums up to 0.


// Constraints:

// 3 <= nums.length <= 3000
// -105 <= nums[i] <= 105

// ## MY SOLUTION : INCOMPLETE

var threeSum = function(nums) {
    nums.sort((a,b) => a -b)

    let i = 0;
    const output = [];
    console.log(nums)
    // we can check only negative numbers
    while( nums[i] <= 0) {
            let sum = - nums[i]
            let l = i + 1;
            let r = nums.length - 1;
            console.log(sum)



            // if the sum is greater than r pointer, no need to check

                while (l < r) {

                // the sum of two pointers greater than sum, should reduce r pointer
                // else, reduce l pointer
                    if (sum === nums[l] + nums[r]) {
                        output.push([nums[i], nums[l], nums[r]])
                        l++;
                        r--;

                    } else {
                        if (sum > nums[l] + nums[r]) {
                            l++;
                        } else {
                            r--;
                        }
                    }

                }
                i++

    }

    return output;

};


// ##SOLUTION 1

function threeSum(nums) {
    const results = [];

    // edge case
    if (nums.length < 3) return results

    // having the numbers in ascending order will make it easier
    // will be O(NlogN)
    nums.sort((a, b) => a - b)

    // represent the first element of array, don't need to check the last two as the first
    for (let i = 0; i < nums.length - 2; i++) {

        // positive numbers cannot sum to negative numbers
        if (nums[i] > 0) break;

        // skip the nums[i] if it already exsit
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let l = i + 1;
        let r = nums.length - 1;

        while (l < r) {
            let sum = - nums[i]
            if (sum === nums[l] + nums[r]) {
                results.push(nums[i], nums[l], nums[r])

                while (nums[l] === nums[l + 1]) l++;
                while (nums[r] === nums[r + 1]) r++;
                l++;
                r--;

            } else if ( sum < nums[l] + nums[r] ) {
                l ++
            } else {
                r --;
            }



        }

    }

    return results;
}