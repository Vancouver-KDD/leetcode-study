function threeSum(nums: number[]): number[][] {
    const res: number[][] = []
    nums.sort((a, b) => a - b)

    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue
        let j = i + 1
        let k = nums.length - 1
        while (j < k) {
            const target = -(nums[i] + nums[j])
            if (target > nums[k]) {
                j++
            } else if (target < nums[k]) {
                k--
            } else if (target == nums[k]) {
                res.push([nums[i], nums[j], nums[k]])
                j++
                k--
                while (j < k && nums[j] === nums[j - 1]) j++
                while (j < k && k < nums.length - 1 && nums[k] === nums[k + 1]) k--
            }
        }
    }
    return res
}
