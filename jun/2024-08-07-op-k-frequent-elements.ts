function topKFrequent(nums: number[], k: number): number[] {
    const result: number[] = []
    const freq = new Map()
    nums.forEach((num) => {
        freq.set(num, (freq.get(num) | 0) + 1)
    })
    for (let i = 0; i < k; i++) {
        let temp = 0
        freq.forEach((value, key) => {
            if (value > temp) {
                temp = value
                result[i] = key
            }
        })
        freq.delete(result[i])
    }
    return result
}
