function totalFruit(fruits: number[]): number {
    let result = 0
    const { length } = fruits
    if (length <= 2) {
        return length
    }
    let l = 0
    let r = 1
    const freq = new Map([[fruits[l], 1]])
    while (r < length) {
        freq.set(fruits[r], (freq.get(fruits[r]) ?? 0) + 1)
        if (freq.size > 2) {
            freq.set(fruits[l], freq.get(fruits[l]) - 1)
            if (freq.get(fruits[l]) === 0) {
                freq.delete(fruits[l])
            }
            l++
        } else {
            result = Math.max(result, r - l + 1)
        }
        r++
    }
    return result
}
