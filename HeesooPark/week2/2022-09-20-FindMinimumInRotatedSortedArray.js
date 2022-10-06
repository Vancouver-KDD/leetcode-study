/**
 * @param {number[]} nums
 * @return {number}
 */
 var findMin = function(nums) {

    // should be O(log n) -> binary search

    // set the two pointers at 0 and n-1
    // set the guess m in the middle of the range
    let n = nums.length
    let l = 0
    let r = n-1
    let min = nums[0];


    // if nums[m] >= nums[l]
    // m is the part of the l's subarray
    // search right
    // if nums[m] < nums[l]
    // m is the part of the r's subarray
    // search left

    while ( l <= r) {

        if (nums[l] < nums[r]) {
            min = Math.min(min, nums[l])
            break
        }

        let m = Math.floor((l+r) /2)
        console.log(m)
        min = Math.min(min, nums[m])

        if (nums[m] >= nums[l]) {
            l = m + 1;
        } else {
            r = m - 1;
        }
    }

    return min;
}


// ### SOLUTION 2
function findMin(nums) {
    let l = 0;
    let r = nums.length - 1
    let m;

    while (l < r) {
        m = (l + r) / 2;

        if (nums[m] > nums[r]) {
            l = m + 1;
        } else {
            r = m;
        }
    }

    return nums[l]
}