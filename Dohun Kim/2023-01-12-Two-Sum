/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const hashTable = new Map();

    for(let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const diff = target - num;

        if (hashTable.has(diff)) {
            return [i, hashTable.get(diff)];
        } else {
            hashTable.set(num, i);
        }
    }
};