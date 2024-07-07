var twoSum = function(nums, target) {
    let leftIdx = 0;
    let rightIdx = nums.length - 1;
    const copyNums = [...nums].sort((x,y) => x-y);

    while (leftIdx < rightIdx){
        const sum = copyNums[leftIdx] + copyNums[rightIdx];
        if (sum > target){
            rightIdx--;
        } 
        else if (sum < target) {
            leftIdx++;
        } else {
            const firstIdx = nums.indexOf(copyNums[leftIdx]);
            nums[firstIdx] = null;
            const secondIdx = nums.indexOf(copyNums[rightIdx])
            return [firstIdx, secondIdx];
        }
    }
};
