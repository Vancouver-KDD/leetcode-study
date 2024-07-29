function subsets(nums: number[]): number[][] {
    const result: number[][] = []
    const { length } = nums
    function helper(i, subset) {
        if (i >= length) {
            result.push(subset)
            return
        }
        helper(i + 1, [...subset, nums[i]])
        helper(i + 1, [...subset])
    }
    helper(0, [])
    return result
}
