function fourSum(nums: number[], target: number): number[][] {
    const result: number[][] = []
    nums.sort((a, b) => a - b)

    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue
        for (let j = i + 1; j < nums.length - 1; j++) {
            if (j > i + 1 && nums[j] === nums[j - 1]) continue
            let left = j + 1
            let right = nums.length - 1
            while (left < right) {
                const sum = nums[i] + nums[j] + nums[left] + nums[right]
                if (target > sum) {
                    left++
                    while (left < right && nums[left] === nums[left - 1]) left++
                } else if (target < sum) {
                    right--
                    while (left < right && nums[right] === nums[right + 1]) right--
                } else {
                    result.push([nums[i], nums[j], nums[left], nums[right]])
                    left++
                    right--
                    while (left < right && nums[left] === nums[left - 1]) left++
                    while (left < right && nums[right] === nums[right + 1]) right--
                }
            }
        }
    }
    return result
}
