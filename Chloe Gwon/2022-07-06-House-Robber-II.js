/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length === 1) return nums[0];
    return Math.max(robHouse(nums, 0, nums.length-2),
                   robHouse(nums, 1, nums.length-1));
};

function robHouse(nums, start, end){
    var prev1 = 0;
    var prev2 = 0;
    for (var i=start; i<=end; i++){
        var temp = prev1;
        prev1 = Math.max(prev1, prev2 + nums[i]);
        prev2 = temp;
    }
    return prev1;
}
