/*
        Logic: Find the mid point and check if the target is at mid point
        if not check target is lower or higher number
        reduce max or increase min and find mid point again and repeat
*/
var search = function(nums, target) {
    let min = 0;
    let max = nums.length - 1
    let mid;
    while(min <= max){
        mid = min + Math.floor((max - min) / 2);

        if(nums[mid] === target)
            return mid
        if(target > nums[mid])
            min = mid + 1;
        else
            max = mid - 1;
    }
    return -1
};