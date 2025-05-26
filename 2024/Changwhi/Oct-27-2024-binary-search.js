/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let middle = Math.trunc(nums.length / 2)
    console.log(middle)
    let left = 0
    let right = nums.length 
    console.log(right)

    while(left < right){ // left >= right

    if (target == nums[middle]) {
            return middle
    }else if(target > nums[middle]) {
        left = middle + 1
    }else{
        right = middle  -1
    }
       middle =  Math.trunc((left + right) / 2)
    
   

    }
     if (nums[middle] == target) {
        return middle
    }else{
    return -1
    }
}