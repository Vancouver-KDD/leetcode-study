/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {


    let start = 0;
    let end = 0 + k;
    let highestAverage = null;
    let n = nums.length;

    if (k == n) {
        highestAverage = 0;
        for (let i = 0; i < k; i++) {
            highestAverage += nums[i];
        }
        highestAverage /= k;
        return highestAverage;
    }

    while (end <= n) {
        let sum = 0;
        for (let i = start; i < end; i++) {
            sum += nums[i];
        }
        sum /= k;
        start++;
        end++;
        if (highestAverage == null) {
            highestAverage = sum;
        } else {
            highestAverage = Math.max(sum, highestAverage);
        }
    }
    return highestAverage;
};