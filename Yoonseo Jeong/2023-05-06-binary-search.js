var search = function(nums, target) {
    if(!nums || target == undefined || nums.length < 1) return -1

    let startIndex = 0
    let lastIndex = nums.length-1

    while(startIndex <= lastIndex) {
        let midIndex = Math.floor((startIndex + lastIndex) / 2)
        if (target === nums[midIndex]) {
            return midIndex
        }
        else if (target < nums[midIndex]) {
            lastIndex = midIndex - 1
        }
        else if (target > nums[midIndex]) {
            startIndex = midIndex + 1
        }
    }

    return -1

    // complexity
    // time: O(log n)
    // space: O(1)
};
