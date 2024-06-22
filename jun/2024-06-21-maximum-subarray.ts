function maxSubArray(nums: number[]): number {
    let l = 0
    let r
    let result = nums[l]
    let sum = nums[l]
    for (r = 1; r < nums.length; r++) {
        if (sum < 0) {
            sum = 0
            l = r
        }
        sum += nums[r]

        result = Math.max(result, sum)
    }
    return result
}
