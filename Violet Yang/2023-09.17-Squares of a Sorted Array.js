var sortedSquares = function(nums) { // nums = [1,4,6,8..]

    const square = nums.map(el=> el * el)
    return square.sort((a,b) => a-b)
};