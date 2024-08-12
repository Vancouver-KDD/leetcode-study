function topKFrequent(words: string[], k: number): string[] {
    const result: string[] = []
    const freq = new Map()
    words.sort()
    words.forEach((word) => {
        freq.set(word, (freq.get(word) | 0) + 1)
    })
    for (let i = 0; i < k; i++) {
        let max = 0
        freq.forEach((value, key) => {
            if (max < value) {
                max = value
                result[i] = key
            }
        })
        freq.delete(result[i])
    }
    return result
}
