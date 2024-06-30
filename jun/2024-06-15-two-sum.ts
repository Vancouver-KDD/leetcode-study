function twoSum(nums: number[], target: number): number[] {
    let i, j;
    for(i = 0; i < nums.length - 1; i++) {
        for(j = i + 1; j < nums.length; j++) {
            if(nums[i] + nums[j] === target) {
                return [i,j]
            }
        }
    }
};