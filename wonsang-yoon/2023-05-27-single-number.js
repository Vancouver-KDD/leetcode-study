/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    if(!nums )
        return 0
    let single = [];
    for (let i = 0; i < nums.length; i++) {
        if (single.includes(nums[i])) {
            console.log(nums[i])
            single = single.filter(e=> e !== nums[i])
        } else {
            single.push(nums[i])
        }
        console.log(single)
    }
    return single[0]
};