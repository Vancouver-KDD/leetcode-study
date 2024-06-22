function maximumSubarraySum(nums: number[], k: number): number {
    let result = 0
    let l = 0
    if (k === 1) {
        return Math.max(...nums)
    }
    const set = new Set([nums[l]])
    let r
    let temp = nums[l]
    for (r = 1; r < nums.length; r++) {
        if (r - l > k - 1) {
            set.delete(nums[l])
            temp -= nums[l]
            l++
        }
        if (set.has(nums[r])) {
            console.log(nums[l], nums[r], set)
            while (nums[r] !== nums[l] && l < r) {
                set.delete(nums[l])
                temp -= nums[l]
                l++
            }
            while (nums[r] === nums[l] && l < r) {
                set.delete(nums[l])
                temp -= nums[l]
                l++
            }
        }
        set.add(nums[r])
        temp += nums[r]
        if (set.size === k) {
            result = Math.max(result, temp)
        }
    }
    return result
}
