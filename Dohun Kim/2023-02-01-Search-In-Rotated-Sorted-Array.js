/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let [l, r] = [0, nums.length - 1];

    while (l <= r) {
        const mid = (l + r) >> 1;
        const midNum = nums[mid];
        const [leftNum, rightNum] = [nums[l], nums[r]];

        if (midNum === target) return mid;

        if (leftNum <= midNum) {
            const isTargetBetweenLeftAndMid = leftNum <= target && target < midNum;
            isTargetBetweenLeftAndMid ? r = mid - 1 : l = mid + 1;
        }

        if (midNum < leftNum) {
            const isTargetBetweenMidAndRight = midNum < target && target <= rightNum;
            isTargetBetweenMidAndRight ? l = mid + 1 : r = mid - 1;
        }
    }

    return -1;
};