var getConcatenation = function(nums) {
    ///return nums.concat(nums)
    //return [...nums, ...nums] 
    // [[1,2,3], 1,2,3]
    let result = []
    for(let i = 0; i < nums.length; i++){
        result[i]=nums[i]
        result[i+nums.length] = nums[i]
        //[1, 2,_,1,2]
    }
    return result
    //[1,2,3] => [1,2,3,1,2,3]
    // 0,3 1,4 2,5
};