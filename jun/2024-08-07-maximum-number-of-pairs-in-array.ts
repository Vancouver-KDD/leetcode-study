function numberOfPairs(nums: number[]): number[] {
    let pair = 0
    let left = 0
    const map = new Map()
    nums.forEach((num) => {
        map.set(num, (map.get(num) | 0) + 1)
    })
    map.forEach((value, key) => {
        if (value % 2 == 1) {
            left++
        }
        pair += Math.floor(value / 2)
    })
    return [pair, left]
}
